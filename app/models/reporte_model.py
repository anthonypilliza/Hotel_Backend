from pydantic import BaseModel
from typing import List

class LibroDiarioResponse(BaseModel):
    total_ingresos: float
    total_egresos: float
    balance_neto: float
    movimientos: List[dict]

class HuespedActivoResponse(BaseModel):
    nombre_cliente: str
    habitacion: str
    fecha_ingreso: str
    fecha_salida: str

class OcupacionResponse(BaseModel):
    total_habitaciones: int
    habitaciones_ocupadas: int
    habitaciones_libres: int
    porcentaje_ocupacion: str