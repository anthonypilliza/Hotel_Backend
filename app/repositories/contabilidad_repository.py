from app.config.database import movimiento_collection

async def create_egreso(egreso_data: dict):
    # Guardamos el gasto en la colección central de movimientos
    nuevo = await movimiento_collection.insert_one(egreso_data)
    return str(nuevo.inserted_id)