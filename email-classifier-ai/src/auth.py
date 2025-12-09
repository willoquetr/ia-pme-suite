import hashlib
import hmac
import json
import os
from datetime import datetime, timedelta
from typing import Dict, Optional
from src.config import settings
from src.logger import app_logger


class AuthService:
    """Service d'authentification pour multi-users."""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hasher un mot de passe avec SHA256.
        
        Args:
            password: Mot de passe en clair
            
        Returns:
            Hash du mot de passe
        """
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, hash_password: str) -> bool:
        """
        Vérifier un mot de passe contre un hash.
        
        Args:
            password: Mot de passe en clair
            hash_password: Hash du mot de passe
            
        Returns:
            True si correspond
        """
        return AuthService.hash_password(password) == hash_password
    
    @staticmethod
    def create_token(user_id: int, username: str) -> str:
        """
        Créer un token JWT simple.
        
        Args:
            user_id: ID utilisateur
            username: Nom d'utilisateur
            
        Returns:
            Token JWT
        """
        payload = {
            'user_id': user_id,
            'username': username,
            'exp': (datetime.utcnow() + timedelta(days=7)).isoformat()
        }
        
        # Format JWT simple : header.payload.signature
        import base64
        header = base64.b64encode(b'{"alg":"HS256","typ":"JWT"}').decode()
        payload_encoded = base64.b64encode(json.dumps(payload).encode()).decode()
        
        signature = hmac.new(
            settings.jwt_secret_key.encode(),
            f"{header}.{payload_encoded}".encode(),
            hashlib.sha256
        ).hexdigest()
        
        return f"{header}.{payload_encoded}.{signature}"
    
    @staticmethod
    def verify_token(token: str) -> Optional[Dict]:
        """
        Vérifier un token JWT.
        
        Args:
            token: Token à vérifier
            
        Returns:
            Données du payload si valide, None sinon
        """
        try:
            import base64
            header, payload, signature = token.split('.')
            
            # Vérifier la signature
            expected_signature = hmac.new(
                settings.jwt_secret_key.encode(),
                f"{header}.{payload}".encode(),
                hashlib.sha256
            ).hexdigest()
            
            if signature != expected_signature:
                return None
            
            # Décoder le payload
            payload_data = json.loads(base64.b64decode(payload))
            
            # Vérifier l'expiration
            if datetime.fromisoformat(payload_data['exp']) < datetime.utcnow():
                return None
            
            return payload_data
        except Exception as e:
            app_logger.warning(f"Token verification failed: {e}")
            return None


# Créer un utilisateur de démonstration si aucun utilisateur n'existe
def setup_demo_user():
    """Créer un utilisateur de démo pour tester."""
    from src.database import db
    
    users = db.execute_query("SELECT COUNT(*) as count FROM users")
    if users[0]['count'] == 0:
        password_hash = AuthService.hash_password("demo123")
        db.execute_insert(
            """
            INSERT INTO users (username, password_hash, email, company_name, is_admin)
            VALUES (?, ?, ?, ?, ?)
            """,
            ("demo", password_hash, "demo@example.com", "Demo Company", 1)
        )
        app_logger.info("Demo user created (username: demo, password: demo123)")
