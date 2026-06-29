from pydantic import BaseModel
from typing import List, Optional

class ReservaHistorial(BaseModel):
    habitacion: str
    fecha: str
    estado: str

# Datos que pedimos para crear al cliente (RF-03)
class ClienteCreate(BaseModel):
    cedula: str
    nombre: str
    correo: str
    telefono: str

# Datos que devolvemos al consultar
class ClienteResponse(ClienteCreate):
    id: str
    historial_reservas: List[ReservaHistorial] = []

