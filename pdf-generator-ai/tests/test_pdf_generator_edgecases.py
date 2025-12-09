from src.pdf_generator import PDFGenerator


def test_validate_unknown_type():
    ok, msg = PDFGenerator.validate_fields("unknown_type", {})
    assert ok is False
    assert "inconnu" in msg


def test_missing_fields_for_devis():
    ok, msg = PDFGenerator.validate_fields("devis", {"nom_client": "ACME"})
    assert ok is False
    assert "Champs manquants" in msg


def test_default_content_alias_quote():
    content = PDFGenerator._generate_default_content("quote", {"nom_client": "ACME", "description": "Test", "montant": "100"})
    assert "Devis pour" in content
