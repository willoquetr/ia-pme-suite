# 🔌 Guide Intégrations Avancées

Fichier: `integrations.py`

Ce module fournit des intégrations prêtes à l'emploi pour vos 3 applications.

## 📋 Intégrations disponibles

### 1. Gmail API - Lire les emails automatiquement

#### Setup

```bash
# 1. Installer dépendances
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client

# 2. Google Cloud Console
# - Aller à https://console.cloud.google.com/
# - Créer nouveau project
# - Activer "Gmail API"
# - Créer "OAuth 2.0 Client ID" (Desktop app)
# - Télécharger credentials.json
# - Placer dans email-classifier-ai/
```

#### Utilisation

```python
from integrations import GmailIntegration
from email_classifier_ai.src.email_classifier import EmailClassifier

# Initialiser
gmail = GmailIntegration("credentials.json")
gmail.authenticate()

# Récupérer emails non lus
emails = gmail.get_unread_emails(limit=5)

# Classifier chaque email
for email in emails:
    result = EmailClassifier.classify(email['snippet'])
    print(f"{email['subject']} -> {result['category']}")
```

#### Cas d'usage

- Lire emails directement depuis Gmail
- Classifier automatiquement
- Créer labels / dossiers dynamiquement
- Répondre automatiquement

---

### 2. Slack API - Notifications et alertes

#### Setup

```bash
# 1. Installer
pip install slack-sdk

# 2. Slack
# - Aller à https://api.slack.com/
# - Créer nouvelle App
# - Activer "Incoming Webhooks"
# - Ajouter nouveau webhook
# - Copier URL
```

#### Utilisation

```python
from integrations import SlackIntegration

# Initialiser
slack = SlackIntegration(
    webhook_url="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
)

# Envoyer alerte classification
slack.send_classification_alert(
    email_subject="Facture #INV-001",
    category="facture",
    confidence=0.95
)

# Alerte PDF généré
slack.send_pdf_generated(
    doc_type="devis",
    file_name="devis_acme.pdf",
    url="https://your-app.com/files/devis_acme.pdf"
)

# Alerte anomalies Excel
slack.send_analysis_alert(
    sheet_name="Sales",
    anomalies_count=3,
    severity="élevée"
)
```

#### Cas d'usage

- Alerter l'équipe des emails urgents
- Notifier PDF générés
- Signaler anomalies Excel
- Alertes temps réel en Slack

---

### 3. Webhooks - Intégrations tierces

#### Setup

```bash
# Aucune installation supplémentaire
# Utiliser les URLs des services externes

# Exemples:
# Zapier: https://hooks.zapier.com/...
# Make: https://hook.make.com/...
# Custom: https://your-api.com/webhooks/...
```

#### Utilisation

```python
from integrations import WebhookManager

# Initialiser
manager = WebhookManager("https://your-app.com")

# Enregistrer webhooks
manager.register_webhook('email.classified', 'https://zapier.com/hook/xyz')
manager.register_webhook('pdf.generated', 'https://make.com/hook/abc')

# Déclencher événements
manager.on_email_classified("Facture", "facture", 0.95)
manager.on_pdf_generated("devis", 15000)
manager.on_analysis_completed("Sales", [...], [...])
```

#### Cas d'usage

- Intégration Zapier (1000+ apps)
- Intégration Make (automation)
- APIs personnalisées
- CRM intégration
- ERP intégration

---

## 🎯 Scénarios complets

### Scénario 1 : Email Classifier + Slack

```python
from integrations import SlackIntegration
from email_classifier_ai.src.email_classifier import EmailClassifier

slack = SlackIntegration("YOUR_WEBHOOK_URL")

# Classifier email
result = EmailClassifier.classify("Facture pour services...")

# Alerter Slack
if result['confidence'] > 0.8:
    slack.send_classification_alert(
        "Services rendering",
        result['category'],
        result['confidence']
    )
```

**Résultat**: Les emails importants sont notifiés automatiquement à votre équipe Slack

### Scénario 2 : PDF Generator + Webhooks + Zapier

```python
from integrations import WebhookManager, ExternalIntegration
from pdf_generator_ai.src.pdf_generator import PDFGenerator

manager = WebhookManager("https://your-app.com")
manager.register_webhook('pdf.generated', 'https://zapier.com/hook/xyz')

# Générer PDF
success, msg, path = PDFGenerator.generate_pdf("devis", fields)

# Déclencher webhook
if success:
    manager.on_pdf_generated("devis", os.path.getsize(path))
    
    # Zapier peut alors:
    # - Envoyer email au client
    # - Créer CRM entry
    # - Sauvegarder en Google Drive
    # - Enregistrer dans base de données
```

**Résultat**: PDFs générés auto-sauvegardés, emails envoyés, CRM mis à jour

### Scénario 3 : Excel Analyzer + Webhooks + Make

```python
from integrations import WebhookManager
from excel_analyzer_ai.src.excel_analyzer import ExcelAnalyzer

manager = WebhookManager("https://your-app.com")
manager.register_webhook('analysis.completed', 'https://make.com/hook/abc')

# Analyser Excel
results = ExcelAnalyzer.analyze(data)

# Déclencher Make scenario
if len(results['anomalies']) > 0:
    manager.on_analysis_completed(
        "Sales",
        results['anomalies'],
        results['suggestions']
    )
    
    # Make peut alors:
    # - Créer ticket support
    # - Envoyer rapport email
    # - Sauvegarder en Google Sheets
    # - Mettre à jour dashboard Power BI
```

**Résultat**: Anomalies détectées, rapports générés, stakeholders notifiés

---

## 🔐 Configuration sécurisée

### Variables d'environnement

```bash
# .env
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/...
ZAPIER_WEBHOOK_URL=https://hooks.zapier.com/...
MAKE_API_KEY=xxx...
GMAIL_CREDENTIALS_PATH=./credentials.json
```

### Code sécurisé

```python
import os
from dotenv import load_dotenv

load_dotenv()

slack = SlackIntegration(
    webhook_url=os.getenv('SLACK_WEBHOOK_URL')
)

manager = WebhookManager("https://your-app.com")
manager.register_webhook(
    'email.classified',
    os.getenv('ZAPIER_WEBHOOK_URL')
)
```

---

## 🚀 Intégration dans vos apps

### Email Classifier + Slack

Ajouter dans `app.py`:

```python
from integrations import SlackIntegration

slack = SlackIntegration(os.getenv('SLACK_WEBHOOK_URL'))

if classify_btn and email_content:
    result = EmailClassifier.classify(email_content)
    
    # Afficher résultat
    st.write(f"Catégorie: {result['category']}")
    
    # Notifier Slack
    slack.send_classification_alert(
        email_content[:50],
        result['category'],
        result['confidence']
    )
```

### PDF Generator + Webhooks

Ajouter dans `app.py`:

```python
from integrations import WebhookManager

manager = WebhookManager(os.getenv('APP_URL'))
manager.register_webhook('pdf.generated', os.getenv('ZAPIER_WEBHOOK_URL'))

if generate_btn:
    success, msg, path = PDFGenerator.generate_pdf(doc_type, fields)
    
    if success:
        # Déclencher webhook
        manager.on_pdf_generated(doc_type, os.path.getsize(path))
        st.success("PDF généré et webhook déclenché!")
```

### Excel Analyzer + Make

Ajouter dans `app.py`:

```python
from integrations import WebhookManager

manager = WebhookManager(os.getenv('APP_URL'))
manager.register_webhook('analysis.completed', os.getenv('MAKE_WEBHOOK_URL'))

if uploaded_file:
    results = ExcelAnalyzer.analyze(data)
    
    if len(results['anomalies']) > 0:
        # Déclencher Make scenario
        manager.on_analysis_completed(
            sheet_name,
            results['anomalies'],
            results['suggestions']
        )
        st.info("Anomalies détectées - Make notification envoyée!")
```

---

## 📊 Flux d'intégration complet

```
Email arrive
    ↓
Email Classifier
    ↓
Classify + Confiance
    ↓
Slack notification ← (équipe alertée)
    ↓
Webhook Zapier ← (CRM updated, email sent)
    ↓
Historique BD
    ↓
Réponse auto-générée
    ↓
Email envoyé
```

---

## 🔧 Setup par plateforme

### Gmail
1. Google Cloud Console → New project
2. Enable Gmail API
3. Create OAuth 2.0 credentials
4. Download credentials.json
5. Add to app directory

### Slack
1. https://api.slack.com → Create App
2. Incoming Webhooks → Add New Webhook
3. Select channel
4. Copy URL to .env

### Zapier
1. https://zapier.com → Make a Zap
2. Choose Webhook trigger
3. Copy URL
4. Add to integrations.py

### Make
1. https://make.com → Create Scenario
2. Add Webhook trigger
3. Copy URL
4. Activate scenario

---

## 💡 Prochaines étapes

- [ ] Ajouter CRM intégration (HubSpot, Pipedrive)
- [ ] Ajouter Cloud storage (Google Drive, Dropbox)
- [ ] Ajouter Payment (Stripe, PayPal)
- [ ] Ajouter SMS alerts (Twilio)
- [ ] Ajouter Analytics (Mixpanel, Segment)

---

**Status**: ✅ Intégrations prêtes pour production
