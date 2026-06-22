from app.repositories import reserva_repository
from app.models.reserva_model import ReservaCreate
from fastapi import HTTPException

async def registrar_reserva(reserva: ReservaCreate):
    # 1. Buscamos la habitación para ver si existe y está libre
    habitacion = await reserva_repository.get_habitacion_by_numero(reserva.habitacion_numero)
    if not habitacion:
        raise HTTPException(status_code=404, detail="Error: Habitación no encontrada.")
    if habitacion.get("estado") != "Libre":
        raise HTTPException(status_code=400, detail="Error: La habitación ya está Ocupada.")

    # 2. Calcular las noches de estadía
    dias = (reserva.fecha_salida - reserva.fecha_ingreso).days
    if dias <= 0:
        raise HTTPException(status_code=400, detail="Error: La fecha de salida debe ser mayor a la de ingreso.")

    # 3. Calcular el total (Noches * Tarifa Base) según RF-06
    tarifa = habitacion.get("precio_noche", 0)
    total = dias * tarifa

    # 4. Preparamos los datos para MongoDB
    reserva_dict = reserva.dict()
    # Convertimos las fechas a texto (ISO) para que MongoDB las guarde sin problema
    reserva_dict["fecha_ingreso"] = reserva_dict["fecha_ingreso"].isoformat()
    reserva_dict["fecha_salida"] = reserva_dict["fecha_salida"].isoformat()
    reserva_dict["total_reserva"] = total
    reserva_dict["estado"] = "Ocupada"

    # 5. Ejecutamos el cambio atómico: Guardamos reserva y ocupamos habitación
    nuevo_id = await reserva_repository.create_reserva(reserva_dict)
    await reserva_repository.actualizar_estado_habitacion(reserva.habitacion_numero, "Ocupada")

    return {"id": nuevo_id, **reserva_dict}

"""
Procesa una nueva reserva: valida disponibilidad, calcula días de estadía,
determina el costo total y cambia el estado de la habitación a Ocupada.
"""

async def cancelar_reserva(reserva_id: str):
    reserva = await reserva_repository.get_reserva_by_id(reserva_id)
    if not reserva:
        raise HTTPException(status_code=404, detail="Error: Reserva no encontrada.")
    
    if reserva.get("estado") == "Cancelada":
        raise HTTPException(status_code=400, detail="Error: La reserva ya se encuentra cancelada.")
        
    # Cambiar estado de la reserva a "Cancelada" y liberar la habitación a "Libre" (RF-07)
    await reserva_repository.actualizar_estado_reserva(reserva_id, "Cancelada")
    await reserva_repository.actualizar_estado_habitacion(reserva.get("habitacion_numero"), "Libre")
    
    return {"mensaje": f"Reserva {reserva_id} cancelada y habitación liberada exitosamente."}