from fastapi import APIRouter, status
from app.models.habitacion_model import HabitacionCreate, HabitacionResponse
from app.services import habitacion_service
from typing import List

router = APIRouter(prefix="/habitaciones", tags=["Módulo de Habitaciones"])

@router.get("/disponibilidad", response_model=List[HabitacionResponse])
async def ver_matriz_disponibilidad():
    return await habitacion_service.consultar_disponibilidad()

@router.post("/registro", response_model=HabitacionResponse, status_code=status.HTTP_201_CREATED)
async def crear_nueva_habitacion(habitacion: HabitacionCreate):
    return await habitacion_service.registrar_habitacion(habitacion)