from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
# Otra forma mucho más segura de trabajar = secret
# "semilla" q podemos generar q sólo conozca nuestro backend q haga q la encriptación y desencriptación use una "semilla" q solo nosotros conocemos y sea más seguro, porq en el proceso de encriptación usa una clave q sólo nosotros conocemos. Cómo generarla? Consultar documentación de fastAPI:
# ejecutar este código en bash:
# openssl rand -hex 32
SECRET = "23cf9708080157dddc1673c5895373bcf36e42dc2406c08a40c8a1693ee40c0f"

# router = APIRouter()
router = APIRouter(
    prefix="/jwtauth", 
    tags=["jwtauth"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}},
    )

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Definit contexto de encriptación
# schemes > definen el algoritmo de encriptación
# verificar si contraseña q nos entrega el usuario es la misma q tenemos almacenada encriptada
# Ahora en la base de datos se guarda es la contraseña encriptada
# se va a bcrypt generator, se hace hash al str, se graba como pw en users_db
crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mauro": {
        "username": "mauro",
        "full_name": "Andres Mauro",
        "email": "mauro@gmail.com",
        "disabled": False,
        "hashed_password": "$2a$12$HgzNgIzvInujBT0.hN3zpOTrW6OZRVdyL6EMFVsXsgDVa5nrXNLJG"
    },
    "morris": {
        "username": "morris",
        "full_name": "Andrew Morris",
        "email": "morris@gmail.com",
        "disabled": True,
        "hashed_password": "$2a$12$icUO/uGNifuQQn..FUkVDunPWVVY22yDmrynJcLQCzoI3CjZLQJAC"}
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

# Obtener y desencriptar el token
async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    # Comprobar si en estos datos está el username
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception

    except JWTError:
        raise exception
    
    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        # 401 > autenticado pero no está autorizado
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    
    return user

# Implementar operación de autenticación
# Se debe verificar si la contraseña está encriptada o no

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    # verificar contraseña hasheada
    # primero se le pasa la contraseña "original" (q viene en el form)
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    # Dentro de los parámetros de jwt, se tiene cuánto tiempo dura el token, por cuánto tiempo es válido. Calcular fecha de expiración
    # se debe encriptar también el token

    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    # expire = datetime.utcnow() + access_token_expiration # > deprecated
    expire = datetime.now(timezone.utc) + access_token_expiration


    # generalmente fecha de expiración se representa como "exp"
    access_token = {
        "sub": user.username,
        "exp": expire
    }

    # token sin encriptar
    # return {"access_token": access_token, "token_type": "bearer"}
    
    # token encriptado
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user