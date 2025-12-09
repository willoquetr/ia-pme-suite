"""
Integration module - Gmail, Slack, Webhooks
Fournit des intégrations avancées pour les 3 applications
"""

import requests
import json
from typing import Dict, Optional, List
from abc import ABC, abstractmethod


# ============================================================================
# GMAIL INTEGRATION
# ============================================================================

class GmailIntegration:
    """Intégration avec Gmail API (lecture des emails)."""
    
    def __init__(self, credentials_json: str):
        """
        Initialiser Gmail integration.
        
        Args:
            credentials_json: Chemin vers le fichier credentials.json
            
        Note:
            1. Télécharger credentials depuis Google Cloud Console
            2. Partager sur https://console.cloud.google.com/
            3. Activer Gmail API
            4. Créer OAuth 2.0 credentials (Desktop app)
        """
        self.credentials_path = credentials_json
        self.service = None
        
    def authenticate(self):
        """Authentifier avec Google."""
        try:
            from google.auth.transport.requests import Request
            from google.oauth2.service_account import Credentials
            from google_auth_oauthlib.flow import InstalledAppFlow
            
            SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
            
            flow = InstalledAppFlow.from_client_secrets_file(
                self.credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
            from googleapiclient.discovery import build
            self.service = build('gmail', 'v1', credentials=creds)
            
            return True
        except Exception as e:
            print(f"Gmail auth error: {e}")
            return False
    
    def get_unread_emails(self, limit: int = 10) -> List[Dict]:
        """Récupérer les emails non lus."""
        if not self.service:
            return []
        
        try:
            results = self.service.users().messages().list(
                userId='me',
                q='is:unread',
                maxResults=limit
            ).execute()
            
            emails = []
            for message in results.get('messages', []):
                msg = self.service.users().messages().get(
                    userId='me',
                    id=message['id']
                ).execute()
                
                headers = msg['payload']['headers']
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No subject')
                from_addr = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
                
                emails.append({
                    'id': message['id'],
                    'subject': subject,
                    'from': from_addr,
                    'snippet': msg['snippet']
                })
            
            return emails
        except Exception as e:
            print(f"Error fetching emails: {e}")
            return []


# ============================================================================
# SLACK INTEGRATION
# ============================================================================

class SlackIntegration:
    """Intégration avec Slack pour notifications et actions."""
    
    def __init__(self, webhook_url: str, bot_token: Optional[str] = None):
        """
        Initialiser Slack integration.
        
        Args:
            webhook_url: URL du webhook Slack (pour messages)
            bot_token: Token du bot (optionnel, pour actions avancées)
            
        Note:
            1. Créer Slack App sur https://api.slack.com/
            2. Ajouter webhooks
            3. Copier Webhook URL
        """
        self.webhook_url = webhook_url
        self.bot_token = bot_token
    
    def send_message(self, channel: str, text: str, blocks: Optional[List] = None) -> bool:
        """Envoyer un message Slack."""
        try:
            payload = {
                'channel': channel,
                'text': text
            }
            if blocks:
                payload['blocks'] = blocks
            
            response = requests.post(
                self.webhook_url,
                json=payload,
                timeout=10
            )
            
            return response.status_code == 200
        except Exception as e:
            print(f"Slack send error: {e}")
            return False
    
    def send_classification_alert(self, email_subject: str, category: str, confidence: float):
        """Envoyer alerte classification d'email."""
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Nouvel email classifié*\n\n*Sujet:* {email_subject}\n*Catégorie:* {category}\n*Confiance:* {confidence:.0%}"
                }
            }
        ]
        
        return self.send_message('#emails', "Email classifié", blocks)
    
    def send_pdf_generated(self, doc_type: str, file_name: str, url: str):
        """Envoyer notification PDF généré."""
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*PDF généré* 📄\n\nType: {doc_type}\nFichier: {file_name}"
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Télécharger"},
                        "url": url
                    }
                ]
            }
        ]
        
        return self.send_message('#documents', "PDF généré", blocks)
    
    def send_analysis_alert(self, sheet_name: str, anomalies_count: int, severity: str):
        """Envoyer alerte analyse Excel."""
        color = "danger" if severity == "élevée" else "warning"
        
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Anomalies détectées* ⚠️\n\nFeuille: {sheet_name}\nAnomalies: {anomalies_count}\nSévérité: {severity}"
                }
            }
        ]
        
        return self.send_message('#data', "Anomalies Excel", blocks)


# ============================================================================
# WEBHOOK INTEGRATION
# ============================================================================

class WebhookManager:
    """Gestionnaire de webhooks pour intégrations tierces."""
    
    def __init__(self, base_url: str):
        """
        Initialiser webhook manager.
        
        Args:
            base_url: URL de base pour les webhooks (ex: https://your-app.com)
        """
        self.base_url = base_url
        self.webhooks: Dict[str, str] = {}
    
    def register_webhook(self, event_type: str, url: str):
        """Enregistrer un webhook pour un événement."""
        self.webhooks[event_type] = url
    
    def trigger_webhook(self, event_type: str, data: Dict) -> bool:
        """Déclencher un webhook."""
        if event_type not in self.webhooks:
            return False
        
        try:
            response = requests.post(
                self.webhooks[event_type],
                json={
                    'event': event_type,
                    'timestamp': str(None),  # datetime.now().isoformat(),
                    'data': data
                },
                timeout=10
            )
            
            return response.status_code in [200, 201]
        except Exception as e:
            print(f"Webhook trigger error: {e}")
            return False
    
    # Events
    
    def on_email_classified(self, email_subject: str, category: str, confidence: float):
        """Déclencher événement classification email."""
        return self.trigger_webhook('email.classified', {
            'subject': email_subject,
            'category': category,
            'confidence': confidence
        })
    
    def on_pdf_generated(self, doc_type: str, file_size: int):
        """Déclencher événement PDF généré."""
        return self.trigger_webhook('pdf.generated', {
            'type': doc_type,
            'size_bytes': file_size
        })
    
    def on_analysis_completed(self, sheet_name: str, anomalies: List, suggestions: List):
        """Déclencher événement analyse complétée."""
        return self.trigger_webhook('analysis.completed', {
            'sheet': sheet_name,
            'anomalies_count': len(anomalies),
            'suggestions_count': len(suggestions)
        })


# ============================================================================
# ZAPIER / MAKE INTEGRATION
# ============================================================================

class ExternalIntegration:
    """Intégration avec services externes (Zapier, Make, IFTTT)."""
    
    @staticmethod
    def to_zapier(event: str, data: Dict, webhook_url: str) -> bool:
        """
        Envoyer événement à Zapier.
        
        Args:
            event: Nom de l'événement
            data: Données à envoyer
            webhook_url: URL du webhook Zapier
        """
        try:
            payload = {
                'event': event,
                **data
            }
            
            response = requests.post(webhook_url, json=payload, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    @staticmethod
    def to_make(scenario_id: str, data: Dict, api_key: str) -> bool:
        """
        Déclencher scénario Make.
        
        Args:
            scenario_id: ID du scénario
            data: Données à envoyer
            api_key: Clé API Make
        """
        try:
            response = requests.post(
                f"https://hook.make.com/v1/scenarios/{scenario_id}/execute",
                json=data,
                headers={'Authorization': f'Bearer {api_key}'},
                timeout=10
            )
            
            return response.status_code in [200, 201]
        except:
            return False


# ============================================================================
# EXEMPLE D'UTILISATION
# ============================================================================

if __name__ == "__main__":
    # Slack
    slack = SlackIntegration(
        webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
    )
    
    slack.send_classification_alert(
        "Facture #INV-001",
        "facture",
        0.95
    )
    
    # Webhooks
    manager = WebhookManager("https://your-app.com")
    manager.register_webhook('email.classified', 'https://zapier.com/webhook/xyz')
    
    manager.on_email_classified("Test", "facture", 0.95)
    
    print("Intégrations configurées avec succès!")
