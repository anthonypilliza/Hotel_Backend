from unittest.mock import patch

def test_registrar_cliente(client):
    with patch("app.controllers.cliente_controller.cliente_service.registrar_cliente") as mock_service:
        # Debemos enviar TODOS los campos que tu clase ClienteResponse exige
        mock_service.return_value = {
            "id": "12345",
            "cedula": "1234567890",
            "nombre": "Juan Prueba",
            "correo": "juan@test.com",
            "telefono": "0999999999"
        }
        
        response = client.post("/clientes/registro", json={
            "cedula": "1234567890",
            "nombre": "Juan Prueba",
            "correo": "juan@test.com",
            "telefono": "0999999999"
        })
        
        assert response.status_code == 201

def test_consultar_cliente(client):
    with patch("app.controllers.cliente_controller.cliente_repository.get_cliente_by_cedula") as mock_repo:
        # Agregamos '_id' para que el controlador no falle al hacer cliente["_id"]
        mock_repo.return_value = {
            "_id": "123",  # <--- ESTO ES LO QUE FALTABA
            "id": "123",
            "cedula": "1234567890",
            "nombre": "Juan Prueba",
            "correo": "juan@test.com",
            "telefono": "0999999999"
        }
        
        response = client.get("/clientes/1234567890")
        
        assert response.status_code == 200
        assert response.json()["cedula"] == "1234567890"