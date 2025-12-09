# 📄 PDF Generator AI

**Outil intelligent de génération de documents PDF pour PME**

- ⚡ **Générer des documents professionnels en 2 minutes** (au lieu de 30 minutes)
- 🤖 **Contenu généré par l'IA** (Mistral, Ollama, OpenAI)
- 📋 **5 types de documents** prédéfinis (devis, factures, contrats, lettres, rapports)
- 🔐 **Multi-user avec authentification** JWT
- 💾 **Historique complet** avec base de données
- 🎯 **100% gratuit et customizable**

---

## 🎯 Vue d'ensemble

PDF Generator AI automatise la création de documents professionnels pour les PME. Chaque document est généré intelligemment avec l'IA, puis converti en PDF formaté.

### Types de documents supportés

| Type | Utilité | Champs |
|------|---------|--------|
| **Quote** (Devis) | Propositions client | client_name, description, amount, validity_days |
| **Invoice** (Facture) | Demandes de paiement | client_name, invoice_number, amount, due_date |
| **Letter** (Lettre) | Communications officielles | recipient_name, subject, body, signature_name |
| **Contract** (Contrat) | Accords | party_a, party_b, subject, terms, effective_date |
| **Report** (Rapport) | Documentation | report_title, summary, findings, recommendations |

### Objectif métier
- Réduire le temps de création documentde 30 min → 2 min
- Uniformiser la qualité des documents
- Archiver automatiquement tous les documents
- Retracer l'historique complet

---

## 🚀 Installation rapide

### Prérequis
- Python 3.11+
- pip

### Installation locale

```bash
# 1. Cloner/Télécharger
cd pdf-generator-ai

# 2. Environnement Python
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 3. Dépendances
pip install -r requirements.txt

# 4. Configuration
cp .env.example .env
# Éditer .env avec vos clés API

# 5. Lancer
streamlit run app.py
```

**Accès** : http://localhost:8502

**Démo** : Username `demo` / Password `demo123`

### Installation Docker

```bash
docker-compose up -d
# http://localhost:8502
```

---

## ⚙️ Configuration

### LLM Provider

Comme Email Classifier, 3 options gratuites :

```bash
# Option 1: Mistral (recommandé)
LLM_PROVIDER=mistral
MISTRAL_API_KEY=votre_cle_ici

# Option 2: Ollama (local gratuit)
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434

# Option 3: OpenAI (trial gratuit 5$)
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

### Base de données

```bash
DB_TYPE=sqlite
DB_PATH=./data/pdf_generator.db
```

### Paramètres PDF

```bash
APP_NAME=PDF Generator AI
PDF_OUTPUT_DIR=./generated_pdfs
COMPANY_NAME=Votre Entreprise
```

---

## 📖 Utilisation

### 1️⃣ Se connecter

- Username: `demo`
- Password: `demo123`

### 2️⃣ Sélectionner un type de document

Choisir dans le dropdown (Quote, Invoice, etc.)

### 3️⃣ Remplir les informations

Les champs affichés dépendent du type de document.

**Exemple pour Devis** :
- Client Name: "ABC Corporation"
- Description: "Web Design & Development"
- Amount: 5000
- Validity Days: 30

### 4️⃣ Générer le PDF

- **Utiliser l'IA** (recommandé) : Génère un contenu intelligent
- **Sans IA** : Template par défaut

### 5️⃣ Télécharger

Cliquer sur "📥 Télécharger le PDF"

---

## 🔧 Architecture

### Structure des fichiers

```
pdf-generator-ai/
├── app.py                      # Interface Streamlit
├── src/
│   ├── config.py              # Configuration
│   ├── logger.py              # Logging
│   ├── database.py            # BD SQLite
│   ├── auth.py                # Authentification JWT
│   ├── llm_service.py         # Service LLM
│   └── pdf_generator.py       # Génération PDF (cœur)
├── templates/                 # Templates documents
├── database/
│   └── schema.sql             # Schéma BD
├── tests/                     # Tests unitaires
├── requirements.txt           # Dépendances
├── .env.example              # Variables d'env
├── Dockerfile                # Docker
└── docker-compose.yml        # Orchestration
```

### Flux principal

```
Utilisateur remplit formulaire
    ↓
app.py valide les champs
    ↓
PDFGenerator.validate_fields()
    ↓
LLMService.generate_document_content()
    ↓
PDF créé avec ReportLab
    ↓
Sauvegardé en BD + fichier
    ↓
Utilisateur télécharge PDF
```

---

## 🔌 API Service (Python)

```python
from src.pdf_generator import PDFGenerator

# Valider les champs
is_valid, msg = PDFGenerator.validate_fields("invoice", {
    "client_name": "ABC Corp",
    "invoice_number": "INV-001",
    "description": "Services",
    "amount": 1000,
    "due_date": "2025-01-20"
})

# Générer le PDF
success, message, pdf_path = PDFGenerator.generate_pdf(
    doc_type="invoice",
    fields={...},
    use_ai=True  # Utiliser l'IA
)
```

---

## 🧪 Tests

```bash
# Lancer les tests
pytest

# Avec couverture
pytest --cov=src --cov-report=html

# Test spécifique
pytest tests/test_pdf_generator.py -v
```

---

## 📊 Base de données

### Table `generated_documents`
```
id              | INTEGER (PK)
user_id         | INTEGER (FK)
document_type   | TEXT (quote, invoice, etc.)
title           | TEXT
content         | TEXT (JSON des champs)
pdf_path        | TEXT (chemin du fichier)
file_size       | INTEGER
status          | TEXT (completed, failed)
created_at      | TIMESTAMP
```

---

## 🐛 Troubleshooting

### ❌ "Module reportlab not found"
```bash
pip install reportlab==4.0.7
```

### ❌ "PDF generation failed"
- Vérifier que `generated_pdfs/` existe
- Vérifier l'API LLM est accessible
- Consulter les logs

### ❌ "Mistral API error"
- Vérifier la clé API dans `.env`
- Vérifier le quota (3600 req/jour pour gratuit)

---

## 📈 Customization

### Ajouter un nouveau type de document

Modifier `src/pdf_generator.py` :

```python
DOCUMENT_TYPES = {
    "my_document": {
        "title": "My Document",
        "fields": ["field1", "field2", "field3"],
        "description": "Description"
    },
    # ... autres types ...
}
```

### Personnaliser le styling PDF

Dans `pdf_generator.py`, modifier les couleurs et styles :

```python
title_style = ParagraphStyle(
    'CustomTitle',
    fontSize=24,
    textColor=colors.HexColor('#1f4788'),  # Changer la couleur
    spaceAfter=30,
    alignment=1
)
```

---

## 🚀 Déploiement

### Production avec Docker

```bash
docker build -t pdf-generator:latest .
docker run -d \
  --name pdf-generator \
  -p 8502:8502 \
  -e LLM_PROVIDER=mistral \
  -e MISTRAL_API_KEY=your_key \
  -v /data:/app/data \
  pdf-generator:latest
```

### Docker Compose

```bash
cp .env.example .env
nano .env  # Configurer

docker-compose up -d
docker-compose logs -f
```

---

## 📄 License

MIT - Libre d'utilisation

---

## 🤝 Support

Pour des questions, consulter :
- `README.md` (ce fichier)
- `docs/API.md` pour l'intégration
- Tests dans `tests/`
- Logs dans `logs/`

---

**Prêt à générer des documents ?**

```bash
streamlit run app.py
```
