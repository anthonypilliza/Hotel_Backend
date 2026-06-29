from unittest.mock import patch
from datetime import date

def test_registrar_egreso(client):
    # La ruta del patch apunta a 'registrar_egreso' en el servicio
    with patch("app.controllers.contabilidad_controller.contabilidad_service.registrar_egreso") as mock_service:
        # Simulamos la respuesta que espera EgresoResponse
        mock_service.return_value = {
            "id": "egr_001",
            "monto": 50.0,
            "descripcion": "Reparación de aire acondicionado",
            "categoria": "Reparaciones",
            "fecha_registro": date.today(),
            "tipo_movimiento": "Egreso"
        }
        
        # Realizamos la petición POST al endpoint definido en el router
        response = client.post("/contabilidad/egresos", json={
            "monto": 50.0,
            "descripcion": "Reparación de aire acondicionado",
            "categoria": "Reparaciones"
        })
        
        assert response.status_code == 201
        assert response.json()["id"] == "egr_001"
        assert response.json()["tipo_movimiento"] == "Egreso"