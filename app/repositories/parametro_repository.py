from app.config.database import database

# Usaremos una colección pequeña solo para la configuración
config_collection = database.get_collection("configuracion")

async def get_parametros():
    return await config_collection.find_one({"tipo": "general"})

async def update_parametros(datos: dict):
    await config_collection.update_one(
        {"tipo": "general"},
        {"$set": datos},
        upsert=True # Si no existe, lo crea
    )