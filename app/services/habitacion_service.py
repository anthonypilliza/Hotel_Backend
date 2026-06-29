from app.repositories import habitacion_repository
from app.models.habitacion_model import HabitacionCreate

async def consultar_disponibilidad():
    # Esto cumple con el RF-05: Retorna todas para pintar la matriz
    return await habitacion_repository.get_todas_las_habitaciones()

async def registrar_habitacion(habitacion: HabitacionCreate):
    habitacion_dict = habitacion.dict()
    nuevo_id = await habitacion_repository.create_habitacion(habitacion_dict)
    return {"id": nuevo_id, **habitacion_dict}