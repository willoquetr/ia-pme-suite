from src.email_classifier import EmailClassifier
from src import llm_service


def test_short_email_returns_autre():
    res = EmailClassifier.classify("")
    assert res["category"] == "autre"
    assert res["confidence"] == 0.0


def test_provider_returns_unknown_category_monkeypatched(monkeypatch):
    # Simuler un provider qui renvoie une catégorie inconnue
    monkeypatch.setattr("src.llm_service.LLMService.classify_email", lambda x: {"category": "unknown", "confidence": 0.9, "reason": "mock"})
    res = EmailClassifier.classify("Bonjour, je voudrais une facture pour mon achat.")
    # La catégorie inconnue doit être normalisée en 'autre'
    assert res["category"] == "autre"
    # La confiance est transmise depuis le provider
    assert res["confidence"] == 0.9
