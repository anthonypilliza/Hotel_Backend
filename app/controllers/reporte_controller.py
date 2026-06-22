from fastapi import APIRouter
from app.models.reporte_model import LibroDiarioResponse, HuespedActivoResponse, OcupacionResponse
from app.services import reporte_service
from typing import List

router = APIRouter(prefix="/reportes", tags=["Módulo de Reportes y Auditoría"])

@router.get("/libro-diario", response_model=LibroDiarioResponse)
async def reporte_libro_diario():
    return await reporte_service.generar_libro_diario()

@router.get("/huespedes-activos", response_model=List[HuespedActivoResponse])
async def reporte_huespedes_activos():
    return await reporte_service.listar_huespedes_activos()

@router.get("/ocupacion", response_model=OcupacionResponse)
async def reporte_ocupacion():
    return await reporte_service.calcular_ocupacion()