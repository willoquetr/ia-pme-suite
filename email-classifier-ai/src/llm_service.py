import requests
import json
import threading
from typing import Optional, Dict
from abc import ABC, abstractmethod
from src.config import settings
from src.logger import app_logger


class LLMProvider(ABC):
    """Interface abstraite pour les fournisseurs LLM."""
    
    @abstractmethod
    def classify_email(self, email_content: str) -> Dict[str, any]:
        """Classifier un email."""
        pass
    
    @abstractmethod
    def summarize_email(self, email_content: str) -> str:
        """Résumer un email."""
        pass
    
    @abstractmethod
    def generate_response(self, email_content: str, category: str, template: str = "") -> str:
        """Générer une réponse."""
        pass


class MistralProvider(LLMProvider):
    """Provider pour Mistral API (gratuit avec limites)."""
    
    def __init__(self, api_key: str = None):
        """
        Initialiser Mistral.
        
        Args:
            api_key: Clé API Mistral (par défaut depuis config)
        """
        self.api_key = api_key or settings.mistral_api_key
        self.base_url = "https://api.mistral.ai/v1"
        self.model = "mistral-small"
    
    def _make_request(self, prompt: str) -> Optional[str]:
        """Faire une requête à Mistral."""
        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7,
                    "max_tokens": 500
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            app_logger.error(f"Mistral API error: {e}")
            return None


class GroqProvider(LLMProvider):
    """Provider pour Groq API (gratuit, rapide)."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or settings.groq_api_key
        self.base_url = "https://api.groq.com/openai/v1"
        self.model = "mixtral-8x7b-32768"
        # Semaphore to limit concurrent Groq requests in this process
        maxc = getattr(settings, 'groq_max_concurrent', 4)
        self._sema = threading.BoundedSemaphore(maxc)

    def _make_request(self, prompt: str) -> Optional[str]:
        acquired = False
        try:
            acquired = self._sema.acquire(timeout=10)
            if not acquired:
                app_logger.warning("Groq concurrency limit reached, rejecting request")
                return None
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.2,
                    "max_tokens": 2000
                },
                timeout=30
            )
            response.raise_for_status()
            return response.json().get('choices', [])[0].get('message', {}).get('content')
        except Exception as e:
            app_logger.error(f"Groq API error: {e}")
            return None
        finally:
            if acquired:
                try:
                    self._sema.release()
                except Exception:
                    pass

    def classify_email(self, email_content: str) -> Dict[str, any]:
        prompt = f"Classifie cet email en une des catégories: facture, devis, reclamation, spam, information, autre.\nEmail:\n{email_content}\nRéponds au format JSON: {'{'}\"category\": \"...\", \"confidence\": 0.0{'}'}"
        result = self._make_request(prompt)
        if not result:
            return {"category": "autre", "confidence": 0.3}
        try:
            # tenter d'extraire JSON depuis la réponse
            start = result.find('{')
            if start != -1:
                payload = json.loads(result[start:])
                return {"category": payload.get('category', 'autre'), "confidence": float(payload.get('confidence', 0.3))}
        except Exception:
            app_logger.warning("Groq response non JSON, fallback simple")
        # fallback heuristics
        lc = email_content.lower()
        if 'facture' in lc or 'facturé' in lc:
            return {"category": "facture", "confidence": 0.8}
        if 'devis' in lc or 'quotation' in lc:
            return {"category": "devis", "confidence": 0.8}
        if 'réclamation' in lc or 'plainte' in lc:
            return {"category": "reclamation", "confidence": 0.8}
        if 'merci' in lc or 'informations' in lc:
            return {"category": "information", "confidence": 0.6}
        return {"category": "autre", "confidence": 0.3}

    def summarize_email(self, email_content: str) -> str:
        prompt = f"Résume en une phrase l'email suivant:\n{email_content}"
        return self._make_request(prompt) or "Résumé indisponible"

    def generate_response(self, email_content: str, category: str, template: str = "") -> str:
        prompt = f"Génère une réponse courte pour un email catégorisé '{category}'. Contexte: {email_content}\nTemplate: {template}"
        return self._make_request(prompt) or ""
    
    def classify_email(self, email_content: str) -> Dict[str, any]:
        """Classifier un email avec Mistral."""
        prompt = f"""Classifie l'email suivant dans UNE SEULE catégorie.
Catégories: facture, devis, reclamation, spam, information, autre

Email:
{email_content}

Réponds en JSON: {{"category": "...", "confidence": 0.0-1.0, "reason": "..."}}"""
        
        response = self._make_request(prompt)
        if response:
            try:
                # Extraire JSON de la réponse
                import json
                data = json.loads(response)
                return {
                    "category": data.get("category", "autre"),
                    "confidence": data.get("confidence", 0.5),
                    "reason": data.get("reason", "")
                }
            except:
                return {"category": "autre", "confidence": 0.5, "reason": "Erreur de classification"}
        return {"category": "autre", "confidence": 0.3, "reason": "Erreur API"}
    
    def summarize_email(self, email_content: str) -> str:
        """Résumer un email."""
        prompt = f"""Résume l'email suivant en 2-3 phrases:

{email_content}

Résumé:"""
        
        response = self._make_request(prompt)
        return response or "Impossible de résumer"
    
    def generate_response(self, email_content: str, category: str, template: str = "") -> str:
        """Générer une réponse professionnelle."""
        template_instruction = f"En utilisant ce template comme base:\n{template}\n" if template else ""
        
        prompt = f"""Génère une réponse professionnelle à cet email de {category}. Sois concis et courtois.
{template_instruction}

Email original:
{email_content}

Réponse:"""
        
        response = self._make_request(prompt)
        return response or "Impossible de générer une réponse"


class OllamaProvider(LLMProvider):
    """Provider pour Ollama (complètement gratuit, local)."""
    
    def __init__(self, base_url: str = None):
        """
        Initialiser Ollama.
        
        Args:
            base_url: URL Ollama (par défaut http://localhost:11434)
        """
        self.base_url = base_url or settings.ollama_base_url
        self.model = "mistral"  # ou "llama2", "neural-chat", etc.
    
    def _make_request(self, prompt: str) -> Optional[str]:
        """Faire une requête à Ollama."""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.7
                },
                timeout=60
            )
            response.raise_for_status()
            return response.json()['response']
        except Exception as e:
            app_logger.error(f"Ollama API error: {e}")
            return None
    
    def classify_email(self, email_content: str) -> Dict[str, any]:
        """Classifier avec Ollama."""
        prompt = f"""Classifie cet email en: facture, devis, reclamation, spam, information ou autre.

Email: {email_content[:500]}

Catégorie: """
        
        response = self._make_request(prompt)
        if response:
            category = response.strip().lower()
            valid_categories = ["facture", "devis", "reclamation", "spam", "information", "autre"]
            category = category if category in valid_categories else "autre"
            return {
                "category": category,
                "confidence": 0.7,
                "reason": "Classification Ollama"
            }
        return {"category": "autre", "confidence": 0.3, "reason": "Ollama indisponible"}
    
    def summarize_email(self, email_content: str) -> str:
        """Résumer avec Ollama."""
        prompt = f"Résume en 2-3 phrases:\n{email_content[:500]}\n\nRésumé: "
        response = self._make_request(prompt)
        return response or "Impossible de résumer"
    
    def generate_response(self, email_content: str, category: str, template: str = "") -> str:
        """Générer réponse avec Ollama."""
        prompt = f"""Génère une réponse professionnelle à cet email de {category}:

{email_content[:500]}

Réponse: """
        response = self._make_request(prompt)
        return response or "Impossible de générer une réponse"


class LLMService:
    """Service pour choisir le bon provider LLM."""
    
    _provider: Optional[LLMProvider] = None
    
    @classmethod
    def get_provider(cls) -> LLMProvider:
        """Obtenir le provider LLM configuré."""
        if cls._provider is None:
            provider_name = settings.llm_provider.lower()
            
            if provider_name == "mistral":
                cls._provider = MistralProvider()
            elif provider_name == "ollama":
                cls._provider = OllamaProvider()
            elif provider_name == "groq":
                cls._provider = GroqProvider()
            elif provider_name == "openai":
                # OpenAI provider not implemented here; fallback to Mistral for now
                app_logger.info("OpenAI selected but not implemented, using Mistral as fallback")
                cls._provider = MistralProvider()
            else:
                app_logger.warning(f"Provider {provider_name} not implemented, using Ollama")
                cls._provider = OllamaProvider()
            
            app_logger.info(f"LLM Provider initialized: {provider_name}")
        
        return cls._provider
    
    @classmethod
    def classify_email(cls, email_content: str) -> Dict[str, any]:
        """Classifier un email."""
        provider = cls.get_provider()
        return provider.classify_email(email_content)
    
    @classmethod
    def summarize_email(cls, email_content: str) -> str:
        """Résumer un email."""
        provider = cls.get_provider()
        return provider.summarize_email(email_content)
    
    @classmethod
    def generate_response(cls, email_content: str, category: str, template: str = "") -> str:
        """Générer une réponse."""
        provider = cls.get_provider()
        return provider.generate_response(email_content, category, template)
