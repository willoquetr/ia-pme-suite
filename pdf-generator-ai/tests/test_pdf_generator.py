import pytest
from src.pdf_generator import PDFGenerator


class TestPDFGenerator:
    """Tests pour le générateur PDF."""
    
    def test_get_document_types(self):
        """Tester la liste des types de documents."""
        doc_types = PDFGenerator.get_document_types()
        
        assert len(doc_types) > 0
        assert "quote" in doc_types
        assert "invoice" in doc_types
    
    def test_get_required_fields(self):
        """Tester la récupération des champs requis."""
        fields = PDFGenerator.get_required_fields("invoice")
        
        assert len(fields) > 0
        assert "client_name" in fields or "invoice_number" in fields
    
    def test_validate_fields_valid(self):
        """Tester la validation avec champs valides."""
        fields = {
            "client_name": "John Doe",
            "invoice_number": "INV-001",
            "description": "Services",
            "amount": 1000,
            "due_date": "2025-01-20"
        }
        
        is_valid, msg = PDFGenerator.validate_fields("invoice", fields)
        
        assert is_valid
        assert msg == "OK"
    
    def test_validate_fields_missing(self):
        """Tester la validation avec champs manquants."""
        fields = {
            "client_name": "John Doe"
        }
        
        is_valid, msg = PDFGenerator.validate_fields("invoice", fields)
        
        assert not is_valid
        assert "manquants" in msg.lower() or "missing" in msg.lower()
    
    def test_generate_default_content_quote(self):
        """Tester la génération de contenu par défaut pour un devis."""
        fields = {
            "client_name": "ABC Corp",
            "description": "Web Design",
            "amount": 5000,
            "validity_days": 30
        }
        
        content = PDFGenerator._generate_default_content("quote", fields)
        
        assert "ABC Corp" in content
        assert "Web Design" in content
    
    def test_generate_default_content_invoice(self):
        """Tester la génération de contenu par défaut pour une facture."""
        fields = {
            "client_name": "XYZ Inc",
            "invoice_number": "INV-2025-001",
            "description": "Consulting",
            "amount": 2000,
            "due_date": "2025-01-20"
        }
        
        content = PDFGenerator._generate_default_content("invoice", fields)
        
        assert "XYZ Inc" in content
        assert "INV-2025-001" in content
    
    def test_document_type_quote_has_fields(self):
        """Tester que le type quote a des champs."""
        doc_type = PDFGenerator.DOCUMENT_TYPES["quote"]
        
        assert "fields" in doc_type
        assert "title" in doc_type
        assert "description" in doc_type
        assert len(doc_type["fields"]) > 0
