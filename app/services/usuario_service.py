from app.repositories import usuario_repository
from app.models.usuario_model import UsuarioCreate
from fastapi import HTTPException

async def registrar_usuario(usuario: UsuarioCreate):
    # Validamos el rol restrictivo según RF-01
    if usuario.rol not in ["Administrador", "Recepcionista"]:
        raise HTTPException(
            status_code=400, 
            detail="Error: El rol debe ser exclusivamente 'Administrador' o 'Recepcionista'."
        )
    
    usuario_dict = usuario.dict()
    nuevo_id = await usuario_repository.create_usuario(usuario_dict)
    
    return {"id": nuevo_id, **usuario_dict}

async def consultar_usuarios():
    return await usuario_repository.get_all_usuarios()