from fastapi import HTTPException, APIRouter, status
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId

router = APIRouter(
    prefix="/userdb", 
    tags=["userdb"],
    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}},
    )

# Devolver todos los usuarios
@router.get("/", response_model=list[User]) 
async def users():
    # return users_schema(db_client.local.users.find())
    return users_schema(db_client.users.find())

# el id en mongo es un "objectId", se debe crear un objeto id de ese mismo tipo, desde bson
@router.get("/{id}") 
async def user(id: str):
    return search_user("_id", ObjectId(id))
    

@router.get("/") 
async def user(id: str):
    return search_user("_id", ObjectId(id))
    

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED) 
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario ya existe")
    
    user_dict = dict(user)
    # para q el id se encargue de generarlo mongodb propiamente
    del user_dict["id"]

    # se crea el esquema "users" en el directorio de la bd
    # id = db_client.local.users.insert_one(user_dict).inserted_id
    id = db_client.users.insert_one(user_dict).inserted_id

    # comprobar q el id está en la bd
    # el nombre de la clave única q crea mongo se llama _id
    # se debe crear operación para poder convertir el resultado a la entidad User, se crea la carpeta "schemas". Esto porq llega como json
    # new_user = user_schema(db_client.local.users.find_one({"_id": id}))
    new_user = user_schema(db_client.users.find_one({"_id": id}))

    return User(**new_user)

# Actualizar todo el objeto
@router.put("/", response_model=User)
async def user(user: User):

    user_dict = dict(user)
    # El id no se puede actualizar, por eso se elimina:
    del user_dict["id"]

    try:
        # db_client.local.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
        db_client.users.find_one_and_replace({"_id": ObjectId(user.id)}, user_dict)
    except:
        return {"error":"No se ha actualizado el usuario"}
    
    return search_user("_id", ObjectId(user.id))


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def user(id: str):

    # found = db_client.local.users.find_one_and_delete({"_id": ObjectId(id)})
    found = db_client.users.find_one_and_delete({"_id": ObjectId(id)})
        
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    
    

# definir criterio para ver si se inserta usuario en la base de datos: buscar si email existe en la bd
def search_user(field: str, key):
    
    try:
        # user = db_client.local.users.find_one({field: key})
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error":"No se ha encontrado el usuario"}