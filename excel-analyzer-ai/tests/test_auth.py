import pytest
from src.auth import AuthService


class TestAuthService:
    """Tests pour l'authentification."""
    
    def test_hash_password(self):
        """Tester le hashage."""
        hashed = AuthService.hash_password("password123")
        assert hashed != "password123"
        assert len(hashed) == 64
    
    def test_verify_password(self):
        """Tester la vérification."""
        password = "test123"
        hashed = AuthService.hash_password(password)
        assert AuthService.verify_password(password, hashed)
        assert not AuthService.verify_password("wrong", hashed)
    
    def test_create_verify_token(self):
        """Tester les tokens JWT."""
        token = AuthService.create_token(1, "testuser")
        payload = AuthService.verify_token(token)
        
        assert payload is not None
        assert payload['user_id'] == 1
        assert payload['username'] == "testuser"
