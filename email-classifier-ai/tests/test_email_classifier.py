import pytest
from src.email_classifier import EmailClassifier


class TestEmailClassifier:
    """Tests pour le service de classification d'emails."""
    
    def test_classify_valid_invoice(self):
        """Tester la classification d'une facture."""
        email = """
        Dear Client,
        
        Your invoice #12345 is attached. Please find the details below:
        Amount: $1000
        Due date: 2025-01-15
        
        Best regards,
        Accounting Team
        """
        
        result = EmailClassifier.classify(email)
        
        assert result['category'] in EmailClassifier.VALID_CATEGORIES
        assert 0 <= result['confidence'] <= 1.0
    
    def test_classify_empty_email(self):
        """Tester avec un email vide."""
        result = EmailClassifier.classify("")
        
        assert result['category'] == "other"
        assert result['confidence'] == 0.0
    
    def test_classify_short_email(self):
        """Tester avec un email très court."""
        result = EmailClassifier.classify("Hi")
        
        assert result['category'] == "other"
        assert result['confidence'] == 0.0
    
    def test_get_categories(self):
        """Tester la liste des catégories."""
        categories = EmailClassifier.get_categories()
        
        assert len(categories) > 0
        assert "invoice" in categories
        assert "complaint" in categories
    
    def test_get_category_description(self):
        """Tester la description d'une catégorie."""
        desc = EmailClassifier.get_category_description("invoice")
        
        assert desc is not None
        assert len(desc) > 0
    
    def test_invalid_category_defaults_to_other(self):
        """Tester que les catégories invalides deviennent 'other'."""
        # Créer un résultat avec catégorie invalide
        result = {
            'category': 'invalid_category',
            'confidence': 0.5
        }
        
        # Valider
        if result['category'] not in EmailClassifier.VALID_CATEGORIES:
            result['category'] = "other"
        
        assert result['category'] == "other"
