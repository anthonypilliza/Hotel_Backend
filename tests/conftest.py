import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    # Creamos el cliente de prueba que usaremos en todos los tests
    return TestClient(app)