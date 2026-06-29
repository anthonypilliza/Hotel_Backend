from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200

# Usamos patch para evitar que el controlador llame a la base de datos real
@patch("app.controllers.usuario_controller.usuario_service.consultar_usuarios")
def test_usuarios_endpoint(mock_service):
    mock_service.return_value = [] # Simulamos respuesta vacía
    response = client.get("/usuarios") 
    assert response.status_code == 200