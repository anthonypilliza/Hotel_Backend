from app.config.database import usuario_collection

async def get_all_usuarios():
    # Retorna la lista de empleados para la lectura (CRUD)
    usuarios = []
    cursor = usuario_collection.find({})
    async for document in cursor:
        document["id"] = str(document["_id"])
        del document["_id"]
        usuarios.append(document)
    return usuarios

async def create_usuario(usuario_data: dict):
    # Inserta el nuevo perfil en la base de datos
    nuevo = await usuario_collection.insert_one(usuario_data)
    return str(nuevo.inserted_id)