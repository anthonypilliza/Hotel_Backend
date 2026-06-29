from pydantic import BaseModel

class ParametrosHotel(BaseModel):
    nombre_comercial: str
    ruc: str
    direccion: str
    porcentaje_iva: float