from fastapi import APIRouter, status
from app.models.cliente_model import ClienteCreate, ClienteResponse
from app.services import cliente_service

router = APIRouter(prefix="/clientes", tags=["Módulo de Clientes"])

@router.post("/registro", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
async def registrar_nuevo_cliente(cliente: ClienteCreate):
    return await cliente_service.registrar_cliente(cliente)