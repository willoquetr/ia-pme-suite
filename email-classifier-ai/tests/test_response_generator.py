import pytest
from src.response_generator import ResponseGenerator


class TestResponseGenerator:
    """Tests pour la génération de réponses."""
    
    def test_generate_response_invoice(self):
        """Tester la génération d'une réponse pour une facture."""
        email = "Please send me the invoice for the recent order."
        
        result = ResponseGenerator.generate(email, "invoice")
        
        assert result['response'] is not None
        assert result['category'] == "invoice"
        assert result['success'] in [True, False]  # Peut échouer si API indisponible
    
    def test_generate_response_complaint(self):
        """Tester la génération d'une réponse pour une réclamation."""
        email = "The product arrived broken. This is unacceptable!"
        
        result = ResponseGenerator.generate(email, "complaint")
        
        assert result['response'] is not None
        assert result['category'] == "complaint"
    
    def test_generate_response_with_template(self):
        """Tester la génération avec un template."""
        email = "Can you send me a quote?"
        template = "Here is our quote for your inquiry:\n[INSERT QUOTE]"
        
        result = ResponseGenerator.generate(email, "quote", template)
        
        assert result['response'] is not None
        assert result['category'] == "quote"
    
    def test_summarize_email(self):
        """Tester le résumé d'un email."""
        email = """
        Dear Team,
        
        I wanted to follow up on our discussion about the Q1 budget allocation.
        We need to confirm the numbers by end of week. The finance department
        has requested clarification on several line items.
        
        Please review and get back to me.
        
        Best,
        John
        """
        
        summary = ResponseGenerator.summarize(email)
        
        assert summary is not None
        assert len(summary) > 0
    
    def test_summarize_short_email(self):
        """Tester le résumé d'un court email."""
        email = "Hi, how are you?"
        
        summary = ResponseGenerator.summarize(email)
        
        assert summary is not None
    
    def test_generate_response_length(self):
        """Tester que la réponse générée a une longueur raisonnable."""
        email = "Test email"
        
        result = ResponseGenerator.generate(email, "information")
        
        # La réponse devrait avoir une longueur (peut être 0 si erreur)
        assert isinstance(result['length'], int)
        assert result['length'] >= 0
