from app.config.database import movimiento_collection, habitacion_collection, cliente_collection
from bson.objectid import ObjectId

async def obtener_todos_movimientos():
    movimientos = []
    cursor = movimiento_collection.find({})
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        movimientos.append(doc)
    return movimientos

async def obtener_reservas_activas():
    reservas = []
    # Buscamos solo las reservas con estado "Ocupada"
    cursor = movimiento_collection.find({"estado": "Ocupada"})
    async for doc in cursor:
        reservas.append(doc)
    return reservas

async def obtener_cliente_por_id(cliente_id: str):
    return await cliente_collection.find_one({"_id": ObjectId(cliente_id)})

async def obtener_metricas_habitaciones():
    total = await habitacion_collection.count_documents({})
    ocupadas = await habitacion_collection.count_documents({"estado": "Ocupada"})
    return total, ocupadas