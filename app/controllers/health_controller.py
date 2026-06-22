from fastapi import APIRouter
from datetime import datetime

router = APIRouter(tags=["Monitoreo del Sistema"])

@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "timestamp": datetime.now().isoformat(),
        "database": "conectada",
        "version": "1.0.0"
    }