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
from typing import Optional

@router.get("/libro-diario", response_model=LibroDiarioResponse)
async def reporte_libro_diario(fecha_inicio: Optional[str] = None, fecha_fin: Optional[str] = None):
    # Obtenemos todos los movimientos del servicio
    reporte_completo = await reporte_service.generar_libro_diario()
    movimientos = reporte_completo["movimientos"]
    
    # Aplicamos el filtro de fechas exigido por el RF-12
    if fecha_inicio and fecha_fin:
        movimientos_filtrados = [
            m for m in movimientos 
            if "fecha_emision" in m and fecha_inicio <= m["fecha_emision"] <= fecha_fin
            or "fecha_registro" in m and fecha_inicio <= m["fecha_registro"] <= fecha_fin
        ]
        
        # Recalculamos los totales con los datos filtrados
        ingresos = sum(float(m.get("total_pagado", 0)) for m in movimientos_filtrados if m.get("tipo_movimiento") == "Factura")
        egresos = sum(float(m.get("monto", 0)) for m in movimientos_filtrados if m.get("tipo_movimiento") == "Egreso")
        
        return {
            "total_ingresos": round(ingresos, 2),
            "total_egresos": round(egresos, 2),
            "balance_neto": round(ingresos - egresos, 2),
            "movimientos": movimientos_filtrados
        }
        
    return reporte_completo