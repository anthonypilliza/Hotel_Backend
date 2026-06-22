from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    nombre: str
    usuario: str
    password: str  # En un entorno real esto iría encriptado
    rol: str       # Obligatorio: "Administrador" o "Recepcionista"

class UsuarioResponse(UsuarioCreate):
    id: str