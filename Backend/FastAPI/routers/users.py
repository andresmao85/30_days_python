from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

# app = FastAPI() # con app, independiente
# con router
router = APIRouter()


# para correr servidor:
# uvicorn users:app --reload


# Creación de entidad para definir usuarios
# se importa "BaseModel"
# Ejm q retorne un json de usuarios 
# (HARD CODED, no OOP)


# @app.get("/usersjson") 
@router.get("/usersjson") 
async def usersjson():
    # return "¡Hola Users!"
    return [
    {"name":"Brais", "surname":"Moure", "url": "www.mouredev.com"},
    {"name":"Juan", "surname":"Perez", "url": "www.juanperez.com"},
    {"name":"Jota", "surname":"Doe", "url": "www.jotadoe.com"}]


# Ahora con OOP
# Entidad user
# BaseModel > da la capacidad de crear una entidad (en este caso una estructura de tipo usuario con los parámetros definidos)

# class User(BaseModel):
#     name: str
#     surname: str
#     url: str
#     age: int

# # Lista en base de datos
# users_list = [
#     User(name= "Brais", surname= "Moure", url= "www.mouredev.com", age= 37), 
#     User(name= "Mauro", surname= "Arias", url= "www.maurodev.com", age= 39),
#     User(name= "Juan", surname= "Perez", url= "www.juanperez.com", age= 24)]

# @app.get("/users") 
@router.get("/users") 
async def users():
    return users_list

# Consulta por PATH (ejm: ID)
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id= 1, name= "Brais", surname= "Moure", url= "www.mouredev.com", age= 37), 
    User(id= 2, name= "Mauro", surname= "Arias", url= "www.maurodev.com", age= 39),
    User(id= 3, name= "Juan", surname= "Perez", url= "www.juanperez.com", age= 24)]

# en thunder client, se hace la prueba a la API con:
# http://127.0.0.1:8000/user/1
# @app.get("/user/{id}") # esto no quiere decir q vamos a llamar a users/id, 
@router.get("/user/{id}") 
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    return search_user(id)
    

# Consulta por QUERY
# en thunder client, se hace la prueba con:
# http://127.0.0.1:8000/userquery/?id=1
# @app.get("/user/") 
@router.get("/user/") 
async def user(id: int):
    return search_user(id)
    
# # http://127.0.0.1:8000/userquery/?id=brais > genera error 422 (unprocessable entity)
'''
"msg": "Input should be a valid integer, unable to parse string as an integer",
"input": "juan"
'''

# Ahora convirtiendo a función el search
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    
'''Cuándo usar path o query
PATH > cuando el parámetro es prácticamente obligatorio (fijo), o q la url puede ser dinámica, ejm: user/1/cars/matricula
QUERY > el parámetro puede ir o no ir (opcional)'''


# MONTAR OPERACIÓN PARA AÑADIR USUARIOS
# En thunder client, para usar la operación POST; se selecciona la tab "Body", y la url de user:
# http://127.0.0.1:8000/user/
# @app.post("/user/") # sin status http
# @app.post("/user/", status_code=201) # con status http
# @app.post("/user/", response_model=User, status_code=201) # con status http y response model
@router.post("/user/", response_model=User, status_code=201) 
async def user(user: User):
    if type(search_user(user.id)) == User:
        # return {"error": "El uuario ya existe"} # sin HTTPException
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        
    
    users_list.append(user)
    return user

# Actualizar objeto: PUT -actualiza el usuario completo (para parte concreta del objeto se utilizaría PATCH, pero no se verá en este curso, investigar)
# @app.put("/user/")
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found: # no es el manejo ideal, se verá el mejor más adelante
        return {"error":"No se ha actualizado el usuario"}
    else:
        return user


# Eliminar objeto: DELETE
# @app.delete("/user/{id}")
@router.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
        
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    else:
        return "Se ha eliminado el usuario"