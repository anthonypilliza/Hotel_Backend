from unittest.mock import patch

def test_registrar_usuario(client):
    with patch("app.controllers.usuario_controller.usuario_service.registrar_usuario") as mock_service:
        mock_service.return_value = {
            "id": "usr_001",
            "nombre": "Admin Test",
            "usuario": "admin",
            "password": "123",
            "rol": "Administrador"
        }
        
        response = client.post("/usuarios/registro", json={
            "nombre": "Admin Test",
            "usuario": "admin",
            "password": "123",
            "rol": "Administrador"
        })
        
        assert response.status_code == 201
        assert response.json()["id"] == "usr_001"

def test_listar_usuarios(client):
    with patch("app.controllers.usuario_controller.usuario_service.consultar_usuarios") as mock_service:
        mock_service.return_value = [
            {"id": "usr_001", "nombre": "Admin", "usuario": "admin", "password": "123", "rol": "Administrador"}
        ]
        
        response = client.get("/usuarios/")
        
        assert response.status_code == 200
        assert len(response.json()) > 0