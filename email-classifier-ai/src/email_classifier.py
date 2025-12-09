from typing import Dict, List
from src.llm_service import LLMService
from src.logger import app_logger


class EmailClassifier:
    """Service de classification d'emails."""
    
    VALID_CATEGORIES = [
        "facture",
        "devis",
        "reclamation",
        "spam",
        "information",
        "autre"
    ]
    
    @classmethod
    def classify(cls, email_content: str) -> Dict[str, any]:
        """
        Classifier un email.
        
        Args:
            email_content: Contenu de l'email
            
        Returns:
            Résultat de classification avec catégorie et confiance
        """
        if not email_content or len(email_content.strip()) < 10:
            return {
                "category": "autre",
                "confidence": 0.0,
                "reason": "Email trop court"
            }
        
        result = LLMService.classify_email(email_content)
        
        # Valider la catégorie
        if result.get('category') not in cls.VALID_CATEGORIES:
            result['category'] = "autre"
        
        app_logger.info(f"Email classified as: {result['category']} (confidence: {result['confidence']})")
        return result
    
    @classmethod
    def get_categories(cls) -> List[str]:
        """Retourner les catégories disponibles."""
        return cls.VALID_CATEGORIES
    
    @classmethod
    def get_category_description(cls, category: str) -> str:
        """Obtenir la description d'une catégorie."""
        descriptions = {
            "facture": "Factures et documents de facturation",
            "devis": "Devis et estimations",
            "reclamation": "Réclamations et problèmes clients",
            "spam": "Spam et emails non pertinents",
            "information": "Informations générales",
            "autre": "Autres types d'emails"
        }
        return descriptions.get(category, "Catégorie inconnue")
