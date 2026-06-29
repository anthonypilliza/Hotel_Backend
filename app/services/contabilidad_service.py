from app.repositories import contabilidad_repository
from app.models.contabilidad_model import EgresoCreate
from datetime import date

async def registrar_egreso(egreso: EgresoCreate):
    egreso_dict = egreso.dict()
    # Agregamos automáticamente la fecha y etiquetamos el tipo de movimiento
    egreso_dict["fecha_registro"] = date.today().isoformat()
    egreso_dict["tipo_movimiento"] = "Egreso"
    
    nuevo_id = await contabilidad_repository.create_egreso(egreso_dict)
    
    return {"id": nuevo_id, **egreso_dict}