from pydantic import BaseModel
from datetime import date
from typing import Optional

class ReservaCreate(BaseModel):
    cliente_id: str
    habitacion_numero: str
    fecha_ingreso: date
    fecha_salida: date

class ReservaResponse(ReservaCreate):
    id: str
    total_reserva: float
    estado: str = "Ocupada"