from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os
# URL de conexión a MongoDB (local por defecto)
load_dotenv()
MONGO_DETAILS = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)


# Nombre de la base de datos
database = client.hotel_ups

# Instanciamos las colecciones según el Apéndice A del documento ERS
usuario_collection = database.get_collection("usuarios")
cliente_collection = database.get_collection("clientes")
habitacion_collection = database.get_collection("habitaciones")
movimiento_collection = database.get_collection("movimientos")