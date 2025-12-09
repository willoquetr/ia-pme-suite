import pytest
from src.auth import AuthService


class TestAuthService:
    """Tests pour l'authentification."""
    
    def test_hash_password(self):
        """Tester le hashage."""
        hashed = AuthService.hash_password("password123")
        
        assert hashed != "password123"
        assert len(hashed) == 64
    
    def test_verify_password_correct(self):
        """Tester la vérification correcte."""
        password = "test123"
        hashed = AuthService.hash_password(password)
        
        assert AuthService.verify_password(password, hashed)
    
    def test_verify_password_incorrect(self):
        """Tester la vérification incorrecte."""
        hashed = AuthService.hash_password("correct")
        
        assert not AuthService.verify_password("wrong", hashed)
    
    def test_create_token(self):
        """Tester la création de token."""
        token = AuthService.create_token(1, "test_user")
        
        assert token is not None
        assert len(token.split('.')) == 3
    
    def test_verify_token(self):
        """Tester la vérification de token."""
        token = AuthService.create_token(1, "test_user")
        payload = AuthService.verify_token(token)
        
        assert payload is not None
        assert payload['user_id'] == 1
        assert payload['username'] == "test_user"
