from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    """Configuration - Excel Analyzer."""
    
    llm_provider: Literal["mistral", "openai", "groq", "ollama"] = "mistral"
    mistral_api_key: str = ""
    openai_api_key: str = ""
    groq_api_key: str = ""
    # Concurrency control for Groq provider (per process)
    groq_max_concurrent: int = 4
    ollama_base_url: str = "http://localhost:11434"
    
    db_type: Literal["sqlite", "postgresql"] = "sqlite"
    db_path: str = "./data/excel_analyzer.db"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "excel_analyzer"
    db_user: str = "postgres"
    db_password: str = ""
    
    jwt_secret_key: str = "dev-secret-key-change-in-production"
    
    app_name: str = "Excel Analyzer AI"
    app_version: str = "1.0.0"
    debug: bool = False
    log_level: str = "INFO"
    
    max_file_size_mb: int = 50
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
