from fastapi import APIRouter, status
from typing import List
from app.models.usuario_model import UsuarioCreate, UsuarioResponse
from app.services import usuario_service

router = APIRouter(prefix="/usuarios", tags=["Módulo de Seguridad (Personal)"])

@router.post("/registro", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
async def registrar_personal(usuario: UsuarioCreate):
    return await usuario_service.registrar_usuario(usuario)

@router.get("/", response_model=List[UsuarioResponse])
async def listar_personal():
    return await usuario_service.consultar_usuarios()

@router.put("/{usuario_id}", status_code=status.HTTP_200_OK)
async def actualizar_personal(usuario_id: str, usuario: UsuarioCreate):
    # Lógica directa en el controlador para agilizar
    from app.config.database import usuario_collection
    from bson.objectid import ObjectId
    from fastapi import HTTPException
    
    if usuario.rol not in ["Administrador", "Recepcionista"]:
        raise HTTPException(status_code=400, detail="Rol inválido.")
        
    resultado = await usuario_collection.update_one(
        {"_id": ObjectId(usuario_id)},
        {"$set": usuario.dict()}
    )
    if resultado.modified_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado o sin cambios.")
    return {"mensaje": "Usuario actualizado exitosamente"}

@router.delete("/{usuario_id}", status_code=status.HTTP_200_OK)
async def desactivar_personal(usuario_id: str):
    from app.config.database import usuario_collection
    from bson.objectid import ObjectId
    from fastapi import HTTPException
    
    # En lugar de borrarlo, lo desactivamos cambiando su rol o agregando un estado
    resultado = await usuario_collection.update_one(
        {"_id": ObjectId(usuario_id)},
        {"$set": {"estado": "Inactivo"}}
    )
    if resultado.modified_count == 0:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")
    return {"mensaje": "Usuario desactivado del sistema"}