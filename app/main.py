from fastapi import FastAPI
from app.controllers import cliente_controller, habitacion_controller, reserva_controller, factura_controller, usuario_controller,contabilidad_controller, reporte_controller, parametro_controller


app = FastAPI(
    title="Sistema de Reserva de Hoteles UPS",
    description="API para la gestión de reservas, habitaciones y facturación.",
    version="1.0.0"
)

# Conectamos el controlador de clientes
app.include_router(cliente_controller.router)
app.include_router(habitacion_controller.router)
app.include_router(reserva_controller.router)
app.include_router(factura_controller.router)
app.include_router(usuario_controller.router)
app.include_router(contabilidad_controller.router)
app.include_router(reporte_controller.router)
app.include_router(parametro_controller.router)
@app.get("/")
async def root():
    return {"mensaje": "¡Servidor de Reservas Hotel UPS en línea!"}