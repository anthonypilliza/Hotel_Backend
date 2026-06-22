from app.repositories import parametro_repository
from app.models.parametro_model import ParametrosHotel

async def guardar_parametros(parametros: ParametrosHotel):
    datos = parametros.dict()
    await parametro_repository.update_parametros(datos)
    return {"mensaje": "Parámetros del hotel actualizados correctamente.", "datos": datos}

async def leer_parametros():
    datos = await parametro_repository.get_parametros()
    if not datos:
        # Valores por defecto si no se ha configurado
        return {"nombre_comercial": "Hotel UPS", "ruc": "9999999999001", "direccion": "S/N", "porcentaje_iva": 0.15}
    del datos["_id"]
    return datos