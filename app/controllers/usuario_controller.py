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