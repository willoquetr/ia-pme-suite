import requests
from typing import Optional, Dict
import threading
from abc import ABC, abstractmethod
from src.config import settings
from src.logger import app_logger


class LLMProvider(ABC):
    """Interface abstraite pour les fournisseurs LLM."""
    
    @abstractmethod
    def generate_document_content(self, doc_type: str, fields: Dict) -> str:
        """Générer le contenu d'un document."""
        pass


class MistralProvider(LLMProvider):
    """Provider pour Mistral API."""
    
    def __init__(self, api_key: str = None):
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
                    "temperature": 0.5,
                    "max_tokens": 2000
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
                    "temperature": 0.3,
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

    def generate_document_content(self, doc_type: str, fields: Dict) -> str:
        fields_text = "\n".join([f"- {k}: {v}" for k, v in fields.items()])
        prompt = f"Génère le contenu pour un document de type {doc_type} avec les champs:\n{fields_text}\nRéponds en texte brut adapté pour un PDF professionnel."
        result = self._make_request(prompt)
        return result or f"Contenu par défaut pour {doc_type}"
    
    def generate_document_content(self, doc_type: str, fields: Dict) -> str:
        """Générer le contenu du document."""
        fields_text = "\n".join([f"- {k}: {v}" for k, v in fields.items()])
        
        prompt = f"""Génère un document {doc_type} professionnel avec les informations suivantes:

{fields_text}

Crée un contenu bien formaté et professionnel. Sois concis et courtois."""
        
        response = self._make_request(prompt)
        return response or "Impossible de générer le contenu"


class OllamaProvider(LLMProvider):
    """Provider pour Ollama."""
    
    def __init__(self, base_url: str = None):
        self.base_url = base_url or settings.ollama_base_url
        self.model = "mistral"
    
    def _make_request(self, prompt: str) -> Optional[str]:
        """Faire une requête à Ollama."""
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.5
                },
                timeout=60
            )
            response.raise_for_status()
            return response.json()['response']
        except Exception as e:
            app_logger.error(f"Ollama API error: {e}")
            return None
    
    def generate_document_content(self, doc_type: str, fields: Dict) -> str:
        """Générer le contenu du document."""
        fields_text = "\n".join([f"- {k}: {v}" for k, v in fields.items()])
        
        prompt = f"""Génère un {doc_type} professionnel avec ces détails:
{fields_text}

Contenu:"""
        
        response = self._make_request(prompt)
        return response or "Impossible de générer le contenu"


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
                app_logger.info("OpenAI selected but not implemented, using Mistral as fallback")
                cls._provider = MistralProvider()
            else:
                app_logger.warning(f"Provider {provider_name} not implemented, using Ollama")
                cls._provider = OllamaProvider()
            
            app_logger.info(f"LLM Provider initialized: {provider_name}")
        
        return cls._provider
    
    @classmethod
    def generate_document_content(cls, doc_type: str, fields: Dict) -> str:
        """Générer le contenu d'un document."""
        provider = cls.get_provider()
        return provider.generate_document_content(doc_type, fields)
