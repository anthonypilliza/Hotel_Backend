from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_habitacion(client):
    # La ruta del patch apunta a 'registrar_habitacion' en el servicio
    with patch("app.controllers.habitacion_controller.habitacion_service.registrar_habitacion") as mock_service:
        mock_service.return_value = {
            "id": "hab_123",
            "numero": "101",
            "tipo": "Simple",
            "precio_noche": 50.0,
            "estado": "Libre"
        }
        
        response = client.post("/habitaciones/registro", json={
            "numero": "101",
            "tipo": "Simple",
            "precio_noche": 50.0,
            "estado": "Libre"
        })
        
        assert response.status_code == 201
        assert response.json()["id"] == "hab_123"

def test_ver_disponibilidad(client):
    # La ruta del patch apunta a 'consultar_disponibilidad' en el servicio
    with patch("app.controllers.habitacion_controller.habitacion_service.consultar_disponibilidad") as mock_service:
        mock_service.return_value = [
            {"id": "hab_123", "numero": "101", "tipo": "Simple", "precio_noche": 50.0, "estado": "Libre"}
        ]
        
        response = client.get("/habitaciones/disponibilidad")
        
        assert response.status_code == 200
        assert len(response.json()) > 0
        assert response.json()[0]["numero"] == "101"