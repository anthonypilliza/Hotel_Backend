from fastapi import APIRouter, status
from app.models.factura_model import FacturaCreate, FacturaResponse
from app.services import factura_service

router = APIRouter(prefix="/facturas", tags=["Módulo de Facturación"])

@router.post("/checkout", response_model=FacturaResponse, status_code=status.HTTP_201_CREATED)
async def realizar_checkout_y_facturar(factura: FacturaCreate):
    return await factura_service.registrar_factura(factura)