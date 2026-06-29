from unittest.mock import patch



def test_registrar_reserva(client):
    # La ruta es /reservas/registro
    with patch("app.controllers.reserva_controller.reserva_service.registrar_reserva") as mock_service:
        mock_service.return_value = {
            "id": "reserva_123",
            "cliente_id": "cli_999", # Agregado
            "habitacion_numero": "101",
            "fecha_ingreso": "2026-07-01",
            "fecha_salida": "2026-07-05",
            "total_reserva": 200.0,
            "estado": "Ocupada"
        }
        
        # Enviamos los campos que exige ReservaCreate
        response = client.post("/reservas/registro", json={
            "cliente_id": "cli_999", # <--- ESTO ES LO QUE FALTABA
            "habitacion_numero": "101",
            "fecha_ingreso": "2026-07-01",
            "fecha_salida": "2026-07-05"
        })
        
        assert response.status_code == 201 
        assert response.json()["id"] == "reserva_123"

def test_cancelar_reserva(client):
    # La ruta es /reservas/{reserva_id}/cancelar
    with patch("app.controllers.reserva_controller.reserva_service.cancelar_reserva") as mock_service:
        mock_service.return_value = {"mensaje": "Reserva reserva_123 cancelada y habitación liberada exitosamente."}
        
        response = client.patch("/reservas/reserva_123/cancelar")
        
        assert response.status_code == 200
        assert "exitosamente" in response.json()["mensaje"]