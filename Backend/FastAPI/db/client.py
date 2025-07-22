from pymongo import MongoClient

# recibe muchos parámetros; si no se incluye ninguno, se conecta a la bd local (localhost)

# ejercicio inicial: se crea el client y en cada uso se hace referencia a local
# db_client = MongoClient()

# mejora: se referencia directamente local:
# db_client = MongoClient().local

# Base de datos remota
db_client = MongoClient("mongodb+srv://test1:test1@cluster0.zvqlifs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test1