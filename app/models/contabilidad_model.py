from pydantic import BaseModel
from datetime import date

class EgresoCreate(BaseModel):
    monto: float
    descripcion: str
    categoria: str # Ej: "Servicios Básicos", "Suministros", "Reparaciones"

class EgresoResponse(EgresoCreate):
    id: str
    fecha_registro: date
    tipo_movimiento: str = "Egreso"