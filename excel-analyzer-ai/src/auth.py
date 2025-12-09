import hashlib
import hmac
import json
from datetime import datetime, timedelta
from typing import Dict, Optional
from src.config import settings
from src.logger import app_logger


class AuthService:
    """Service d'authentification."""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hasher un mot de passe."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    @staticmethod
    def verify_password(password: str, hash_password: str) -> bool:
        """Vérifier un mot de passe."""
        return AuthService.hash_password(password) == hash_password
    
    @staticmethod
    def create_token(user_id: int, username: str) -> str:
        """Créer un token JWT."""
        payload = {
            'user_id': user_id,
            'username': username,
            'exp': (datetime.utcnow() + timedelta(days=7)).isoformat()
        }
        
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
        """Vérifier un token JWT."""
        try:
            import base64
            header, payload, signature = token.split('.')
            
            expected_signature = hmac.new(
                settings.jwt_secret_key.encode(),
                f"{header}.{payload}".encode(),
                hashlib.sha256
            ).hexdigest()
            
            if signature != expected_signature:
                return None
            
            payload_data = json.loads(base64.b64decode(payload))
            
            if datetime.fromisoformat(payload_data['exp']) < datetime.utcnow():
                return None
            
            return payload_data
        except Exception as e:
            app_logger.warning(f"Token verification failed: {e}")
            return None


def setup_demo_user():
    """Créer un utilisateur de démo."""
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
        app_logger.info("Demo user created")
