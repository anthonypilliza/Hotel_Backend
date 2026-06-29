from app.repositories import cliente_repository
from app.models.cliente_model import ClienteCreate
from fastapi import HTTPException

async def registrar_cliente(cliente: ClienteCreate):
    # 1. Validar RF-03: que el documento no esté duplicado
    existente = await cliente_repository.get_cliente_by_cedula(cliente.cedula)
    if existente:
        raise HTTPException(status_code=400, detail="Error: La cédula ya está registrada.")
    
    # 2. Si todo está bien, lo preparamos para guardar
    cliente_dict = cliente.dict()
    nuevo_id = await cliente_repository.create_cliente(cliente_dict)
    
    # 3. Retornamos los datos con el ID generado
    return {"id": nuevo_id, **cliente_dict, "historial_reservas": []}