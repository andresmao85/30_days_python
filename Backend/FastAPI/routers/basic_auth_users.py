from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
# Importar módulo de autenticación
# bearer > se encarga de gestionar autenticación, usuario y contraseña
# request form > cómo se van a enviar al backend los criterios de autenticación (capturar usuario y contra)
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

# Instancia del sistema de autenticación
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

# entidad para representar al usuario de BD
# (User) >  se heredan las propiedades, se añade pw
class UserDB(User):
    password: str


users_db = {
    "mauro": {
        "username": "Mauro",
        "full_name": "Andres Mauro",
        "email": "mauro@gmail.com",
        "disabled": False,
        "password": "12345"
    },
    "morris": {
        "username": "Morris",
        "full_name": "Andrew Morris",
        "email": "morris@gmail.com",
        "disabled": True,
        "password": "54321"
    }
}

# función para determinar si usuario existe
def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])
    
# implementación criterio de dependencia
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        # 401 > autenticado pero no está autorizado
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})
    
    if user.disabled:
        # 401 > autenticado pero no está autorizado
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    
    return user

# implementar operación de autenticación
# operación > voy a obtener datos pero gracias a q se envían datos, en concreto, usuario y contra, por lo cual se usa post

# Depends > la operación va a recibir datos pero no depende de nada
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    # si existe el usuario, se retorna un access token, y de q tipo. Normalmente es algo encriptado para interactuar con el backend
    return {"access_token": user.username, "token_type": "bearer"}

# Ya autenticado, obtener datos de usuarios
# criterios de dependencia > depende de q el usuario esté autenticado. Podemos implementar operaciones q validen la op
# ver criterio de dependencia definido arriba
@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

'''
prueba en thunder client
1-
tipo get
http://127.0.0.1:8000/users/me > lo gestiona directamente fastapi, Status: 401 Unauthorized, "detail": "Not authenticated"

2- 
tipo post
http://127.0.0.1:8000/login
"Body" en thunder, luego "form", agregar username y pw
mauro - 12345

retorna:
{
  "access_token": "Morris",
  "token_type": "bearer"
}

3-
tipo get
http://127.0.0.1:8000/users/me
{
  "detail": "Not authenticated"
}
para q funcione se le debe pasar token
en thunder > "Auth" > "Bearer" = mauro
'''