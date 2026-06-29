from pydantic import BaseModel

class HabitacionCreate(BaseModel):
    numero: str
    tipo: str
    precio_noche: float
    estado: str = "Libre"  # Por defecto siempre inician libres

class HabitacionResponse(HabitacionCreate):
    id: str