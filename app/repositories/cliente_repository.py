from app.config.database import cliente_collection

async def get_cliente_by_cedula(cedula: str):
    # Busca si ya existe alguien con esa cédula
    return await cliente_collection.find_one({"cedula": cedula})

async def create_cliente(cliente_data: dict):
    # Agregamos el historial vacío por defecto
    cliente_data["historial_reservas"] = []
    nuevo_cliente = await cliente_collection.insert_one(cliente_data)
    return str(nuevo_cliente.inserted_id)