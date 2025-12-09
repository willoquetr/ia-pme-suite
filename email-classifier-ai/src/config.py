from pydantic_settings import BaseSettings
from typing import Literal
import os


class Settings(BaseSettings):
    """Configuration centralisée de l'application."""
    
    # LLM
    llm_provider: Literal["mistral", "openai", "groq", "ollama"] = "mistral"
    mistral_api_key: str = ""
    openai_api_key: str = ""
    groq_api_key: str = ""
    # Concurrency control for Groq provider (per process)
    groq_max_concurrent: int = 4
    ollama_base_url: str = "http://localhost:11434"
    
    # Database
    db_type: Literal["sqlite", "postgresql"] = "sqlite"
    db_path: str = "./data/email_classifier.db"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "email_classifier"
    db_user: str = "postgres"
    db_password: str = ""
    
    # Authentication
    jwt_secret_key: str = "dev-secret-key-change-in-production"
    
    # Application
    app_name: str = "Email Classifier AI"
    app_version: str = "1.0.0"
    debug: bool = False
    log_level: str = "INFO"
    
    # Streamlit
    streamlit_port: int = 8501
    streamlit_address: str = "localhost"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Instance globale
settings = Settings()
