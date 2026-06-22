from app.config.database import movimiento_collection
from bson.objectid import ObjectId

async def get_reserva_by_id(reserva_id: str):
    # Recupera de forma automática los datos de la estadía desde la colección movimientos [cite: 339, 410]
    return await movimiento_collection.find_one({"_id": ObjectId(reserva_id)})

async def create_factura_registro(factura_data: dict):
    # Registra de forma transparente la estructura de la transacción financiera [cite: 344, 410]
    nueva = await movimiento_collection.insert_one(factura_data)
    return str(nueva.inserted_id)