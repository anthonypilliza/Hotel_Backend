import pytest
from unittest.mock import AsyncMock, patch
from app.services.usuario_service import consultar_usuarios, registrar_usuario

@pytest.mark.asyncio
async def test_consultar_usuarios_mock():
    # Simulamos el repositorio para que NO intente conectar a MongoDB
    with patch("app.services.usuario_service.usuario_repository.get_all_usuarios", new_callable=AsyncMock) as mock_get:
        # Hacemos que devuelva una lista vacía en lugar de intentar conectar
        mock_get.return_value = []
        usuarios = await consultar_usuarios()
        assert usuarios == []
        assert mock_get.called

@pytest.mark.asyncio
async def test_registrar_usuario_mock():
    with patch("app.services.usuario_service.usuario_repository.create_usuario", new_callable=AsyncMock) as mock_create:
        mock_create.return_value = "fake_id"
        from app.models.usuario_model import UsuarioCreate
        # AJUSTA ESTOS CAMPOS SEGÚN TU MODELO REAL
        u = UsuarioCreate(usuario="testuser", nombre="Test", password="123", rol="Administrador")
        
        resultado = await registrar_usuario(u)
        assert resultado["id"] == "fake_id"