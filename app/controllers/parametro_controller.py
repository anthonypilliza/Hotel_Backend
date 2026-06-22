from fastapi import APIRouter, status
from app.models.parametro_model import ParametrosHotel
from app.services import parametro_service

router = APIRouter(prefix="/configuracion", tags=["Módulo de Configuración de Seguridad"])

@router.put("/parametros", status_code=status.HTTP_200_OK)
async def actualizar_parametros_hotel(parametros: ParametrosHotel):
    return await parametro_service.guardar_parametros(parametros)

@router.get("/parametros")
async def consultar_parametros_hotel():
    return await parametro_service.leer_parametros()