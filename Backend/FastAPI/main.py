from fastapi import FastAPI

app = FastAPI()


@app.get("/") # raíz de la IP donde se esté desplegando la app
async def root():
    return "¡Hola FastAPI!"

@app.get("/url") # raíz de la IP donde se esté desplegando la app
async def url():
    return { "url_curso":"https://mouredev.com"}

# lanzar server:
#    uvicorn main:app --reload

# si se invoca una url q no existe, se obtiene ese msj de error:
# {"detail":"Not Found"}

'''
Creación de documentación automática:
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
'''

### ROUTERS

from routers import products, users
from fastapi.staticfiles import StaticFiles

app.include_router(products.router)
app.include_router(users.router)
app.mount("/aqui", StaticFiles(directory="static"), name="static") # donde se quiere exponer: /lo que sea (ejm static)