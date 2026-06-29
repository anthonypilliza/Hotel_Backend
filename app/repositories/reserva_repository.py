from app.config.database import movimiento_collection, habitacion_collection
from bson.objectid import ObjectId
async def get_habitacion_by_numero(numero: str):
    # Busca la habitación en la base de datos para ver si existe y su estado
    return await habitacion_collection.find_one({"numero": numero})

async def actualizar_estado_habitacion(numero: str, nuevo_estado: str):
    # Cambia el estado de la habitación (ej. de Libre a Ocupada)
    await habitacion_collection.update_one(
        {"numero": numero}, 
        {"$set": {"estado": nuevo_estado}}
    )

async def create_reserva(reserva_data: dict):
    # Guarda la reserva final en la colección de movimientos
    nueva = await movimiento_collection.insert_one(reserva_data)
    return str(nueva.inserted_id)



async def get_reserva_by_id(reserva_id: str):
    return await movimiento_collection.find_one({"_id": ObjectId(reserva_id)})

async def actualizar_estado_reserva(reserva_id: str, nuevo_estado: str):
    await movimiento_collection.update_one(
        {"_id": ObjectId(reserva_id)}, 
        {"$set": {"estado": nuevo_estado}}
    )