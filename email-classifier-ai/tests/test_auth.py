import pytest
from src.auth import AuthService


class TestAuthService:
    """Tests pour le service d'authentification."""
    
    def test_hash_password(self):
        """Tester le hashage de mot de passe."""
        password = "test_password_123"
        hashed = AuthService.hash_password(password)
        
        assert hashed != password
        assert len(hashed) == 64  # SHA256 hex = 64 caractères
    
    def test_verify_password_correct(self):
        """Tester la vérification d'un bon mot de passe."""
        password = "test_password_123"
        hashed = AuthService.hash_password(password)
        
        assert AuthService.verify_password(password, hashed)
    
    def test_verify_password_incorrect(self):
        """Tester la vérification d'un mauvais mot de passe."""
        password = "test_password_123"
        hashed = AuthService.hash_password(password)
        wrong_password = "wrong_password"
        
        assert not AuthService.verify_password(wrong_password, hashed)
    
    def test_create_token(self):
        """Tester la création d'un token JWT."""
        user_id = 1
        username = "testuser"
        
        token = AuthService.create_token(user_id, username)
        
        assert token is not None
        assert len(token.split('.')) == 3  # JWT a 3 parties
    
    def test_verify_token_valid(self):
        """Tester la vérification d'un token valide."""
        user_id = 1
        username = "testuser"
        
        token = AuthService.create_token(user_id, username)
        payload = AuthService.verify_token(token)
        
        assert payload is not None
        assert payload['user_id'] == user_id
        assert payload['username'] == username
    
    def test_verify_token_invalid(self):
        """Tester la vérification d'un token invalide."""
        invalid_token = "invalid.token.here"
        payload = AuthService.verify_token(invalid_token)
        
        assert payload is None
    
    def test_hash_consistency(self):
        """Tester que le même mot de passe produit le même hash."""
        password = "consistent_password"
        hash1 = AuthService.hash_password(password)
        hash2 = AuthService.hash_password(password)
        
        assert hash1 == hash2
