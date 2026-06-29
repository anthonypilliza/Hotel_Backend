from pydantic import BaseModel
from datetime import date

# Esquema para capturar los datos necesarios durante el proceso de Check-out (RF-09) [cite: 340]
class FacturaCreate(BaseModel):
    reserva_id: str
    metodo_pago: str  # Efectivo, Tarjeta de Crédito/Débito o Transferencia Bancaria [cite: 340]

# Esquema de respuesta con los campos comerciales obligatorios del Apéndice A [cite: 339, 423]
class FacturaResponse(BaseModel):
    id: str
    reserva_id: str
    num_factura: str  # Numeración secuencial automática e incremental [cite: 339, 425]
    subtotal: float  # Subtotal neto calculado [cite: 339, 426]
    iva: float  # Valor del Impuesto al Valor Agregado aplicado [cite: 339, 427]
    total_pagado: float  # Monto total final liquidado [cite: 339, 428]
    metodo_pago: str  # Modalidad de pago seleccionada por recepción [cite: 340, 429]
    fecha_emision: date