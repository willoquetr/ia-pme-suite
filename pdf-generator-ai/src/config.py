from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    """Configuration centralisée - PDF Generator."""
    
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
    db_path: str = "./data/pdf_generator.db"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "pdf_generator"
    db_user: str = "postgres"
    db_password: str = ""
    
    # Authentication
    jwt_secret_key: str = "dev-secret-key-change-in-production"
    
    # Application
    app_name: str = "PDF Generator AI"
    app_version: str = "1.0.0"
    debug: bool = False
    log_level: str = "INFO"
    
    # PDF
    pdf_output_dir: str = "./generated_pdfs"
    company_name: str = "Your Company Name"
    company_logo_path: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
