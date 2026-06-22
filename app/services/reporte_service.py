from app.repositories import reporte_repository

async def generar_libro_diario():
    movimientos = await reporte_repository.obtener_todos_movimientos()
    ingresos = 0.0
    egresos = 0.0
    
    for mov in movimientos:
        if mov.get("tipo_movimiento") == "Factura":
            ingresos += float(mov.get("total_pagado", 0))
        elif mov.get("tipo_movimiento") == "Egreso":
            egresos += float(mov.get("monto", 0))
            
    return {
        "total_ingresos": round(ingresos, 2),
        "total_egresos": round(egresos, 2),
        "balance_neto": round(ingresos - egresos, 2),
        "movimientos": movimientos
    }

async def listar_huespedes_activos():
    reservas = await reporte_repository.obtener_reservas_activas()
    huespedes = []
    
    for reserva in reservas:
        cliente_id = reserva.get("cliente_id")
        cliente = await reporte_repository.obtener_cliente_por_id(cliente_id)
        nombre = cliente.get("nombre", "Desconocido") if cliente else "Desconocido"
        
        huespedes.append({
            "nombre_cliente": nombre,
            "habitacion": reserva.get("habitacion_numero"),
            "fecha_ingreso": str(reserva.get("fecha_ingreso")),
            "fecha_salida": str(reserva.get("fecha_salida"))
        })
    return huespedes

async def calcular_ocupacion():
    total, ocupadas = await reporte_repository.obtener_metricas_habitaciones()
    libres = total - ocupadas
    
    porcentaje = (ocupadas / total * 100) if total > 0 else 0.0
    
    return {
        "total_habitaciones": total,
        "habitaciones_ocupadas": ocupadas,
        "habitaciones_libres": libres,
        "porcentaje_ocupacion": f"{round(porcentaje, 2)}%"
    }