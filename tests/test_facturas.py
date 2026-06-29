from unittest.mock import patch
from datetime import date

def test_realizar_checkout_y_facturar(client):
    # El patch debe ir al servicio que el controlador está usando
    with patch("app.controllers.factura_controller.factura_service.registrar_factura") as mock_service:
        # Simulamos la respuesta completa que espera FacturaResponse
        mock_service.return_value = {
            "id": "fact_001",
            "reserva_id": "reserva_123",
            "num_factura": "001-001-123456",
            "subtotal": 173.91,
            "iva": 26.09,
            "total_pagado": 200.0,
            "metodo_pago": "Efectivo",
            "fecha_emision": date.today()
        }
        
        response = client.post("/facturas/checkout", json={
            "reserva_id": "reserva_123",
            "metodo_pago": "Efectivo"
        })
        
        # Verificamos que el checkout y facturación sean exitosos
        assert response.status_code == 201
        assert response.json()["id"] == "fact_001"
        assert response.json()["total_pagado"] == 200.0