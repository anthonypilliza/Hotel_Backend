from fastapi import APIRouter, status
from app.models.reserva_model import ReservaCreate, ReservaResponse
from app.services import reserva_service

router = APIRouter(prefix="/reservas", tags=["Módulo de Reservas"])

@router.post("/registro", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
async def crear_reserva(reserva: ReservaCreate):
    return await reserva_service.registrar_reserva(reserva)

@router.patch("/{reserva_id}/cancelar", status_code=status.HTTP_200_OK)
async def anular_reserva(reserva_id: str):
    return await reserva_service.cancelar_reserva(reserva_id)