from typing import Dict
from src.llm_service import LLMService
from src.logger import app_logger


class ResponseGenerator:
    """Service de génération de réponses automatiques."""
    
    @classmethod
    def generate(cls, email_content: str, category: str, template: str = "") -> Dict[str, str]:
        """
        Générer une réponse automatique.
        
        Args:
            email_content: Contenu de l'email
            category: Catégorie de l'email
            template: Template personnalisé optionnel
            
        Returns:
            Réponse générée avec métadonnées
        """
        try:
            response = LLMService.generate_response(email_content, category, template)
            
            app_logger.info(f"Response generated for {category} email")
            
            return {
                "response": response,
                "category": category,
                "length": len(response),
                "success": True
            }
        except Exception as e:
            app_logger.error(f"Response generation error: {e}")
            return {
                "response": "Unable to generate response. Please try again.",
                "category": category,
                "length": 0,
                "success": False,
                "error": str(e)
            }
    
    @classmethod
    def summarize(cls, email_content: str) -> str:
        """
        Résumer un email.
        
        Args:
            email_content: Contenu de l'email
            
        Returns:
            Résumé de l'email
        """
        try:
            summary = LLMService.summarize_email(email_content)
            app_logger.info(f"Email summarized ({len(summary)} chars)")
            return summary
        except Exception as e:
            app_logger.error(f"Summarization error: {e}")
            return "Unable to summarize email."
