from fastapi.testclient import TestClient
from app.main import app

# Cliente de pruebas que simula peticiones sin levantar el servidor real
client = TestClient(app)

def test_root_endpoint():
    # Simulamos una petición GET a la ruta principal
    response = client.get("/")
    
    # Verificamos que responda HTTP 200 (Éxito)
    assert response.status_code == 200
    
    # Verificamos que el mensaje sea exactamente el esperado
    assert response.json() == {"mensaje": "¡Servidor de Reservas Hotel UPS en línea!"}