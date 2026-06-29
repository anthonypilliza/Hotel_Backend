from fastapi import APIRouter, status
from app.models.contabilidad_model import EgresoCreate, EgresoResponse
from app.services import contabilidad_service

router = APIRouter(prefix="/contabilidad", tags=["Módulo de Contabilidad"])

@router.post("/egresos", response_model=EgresoResponse, status_code=status.HTTP_201_CREATED)
async def registrar_nuevo_egreso(egreso: EgresoCreate):
    return await contabilidad_service.registrar_egreso(egreso)