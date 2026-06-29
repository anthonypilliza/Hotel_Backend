from app.repositories import factura_repository, reserva_repository
from app.models.factura_model import FacturaCreate
from fastapi import HTTPException
from datetime import date
import random

async def registrar_factura(factura: FacturaCreate):
    # 1. Obtener la reserva para el RF-08 
    reserva = await factura_repository.get_reserva_by_id(factura.reserva_id)
    if not reserva:
        raise HTTPException(status_code=404, detail="Error: Reserva no encontrada.")

    # 2. Calcular valores (RF-08) 
    # Asumimos que el total de la reserva ya incluye el IVA (15% en Ecuador) para desglosarlo
    total_reserva = reserva.get("total_reserva", 0)
    subtotal = round(total_reserva / 1.15, 2)
    iva = round(total_reserva - subtotal, 2)

    # 3. Generar número de factura secuencial simulado 
    num_factura = f"001-001-{random.randint(100000, 999999)}"

    # 4. Preparar datos de la factura (RF-09) 
    factura_dict = {
        "reserva_id": factura.reserva_id,
        "num_factura": num_factura,
        "subtotal": subtotal,
        "iva": iva,
        "total_pagado": total_reserva,
        "metodo_pago": factura.metodo_pago,
        "fecha_emision": date.today().isoformat(),
        "tipo_movimiento": "Factura"
    }

    # 5. Guardar la factura
    nuevo_id = await factura_repository.create_factura_registro(factura_dict)

    # 6. Liberar la habitación (Paso 23 del Diagrama de Secuencia) 
    await reserva_repository.actualizar_estado_habitacion(reserva.get("habitacion_numero"), "Libre")

    return {"id": nuevo_id, **factura_dict}