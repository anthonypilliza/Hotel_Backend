from fastapi import APIRouter, status
from app.models.cliente_model import ClienteCreate, ClienteResponse
from app.services import cliente_service
from fastapi import HTTPException
from app.repositories import cliente_repository

router = APIRouter(prefix="/clientes", tags=["Módulo de Clientes"])

@router.post("/registro", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
async def registrar_nuevo_cliente(cliente: ClienteCreate):
    return await cliente_service.registrar_cliente(cliente)



@router.get("/{cedula}", response_model=ClienteResponse)
async def consultar_historial_cliente(cedula: str):
    cliente = await cliente_repository.get_cliente_by_cedula(cedula)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    cliente["id"] = str(cliente["_id"])
    return cliente