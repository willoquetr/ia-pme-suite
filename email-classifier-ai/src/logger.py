import logging
import os
from datetime import datetime


def setup_logger(name: str) -> logging.Logger:
    """
    Configure un logger avec fichier et console.
    
    Args:
        name: Nom du logger
        
    Returns:
        Logger configuré
    """
    # Créer dossier logs si nécessaire
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    # Format commun
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler fichier (audit)
    log_file = f"logs/{name}_{datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Handler console (infos principales)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger


# Logger d'audit
audit_logger = setup_logger("audit")

# Logger applicatif
app_logger = setup_logger("app")
