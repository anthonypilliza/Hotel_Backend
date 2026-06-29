from app.config.database import habitacion_collection

async def get_todas_las_habitaciones():
    habitaciones = []
    cursor = habitacion_collection.find({})
    async for document in cursor:
        document["id"] = str(document["_id"])
        del document["_id"]
        habitaciones.append(document)
    return habitaciones

async def create_habitacion(habitacion_data: dict):
    nueva = await habitacion_collection.insert_one(habitacion_data)
    return str(nueva.inserted_id)