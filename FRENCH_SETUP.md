# 🇫🇷 Configuration 100% Français - Guide complet

Toutes les applications sont maintenant **entièrement en français** :
- ✅ Interface Streamlit (menus, boutons, messages)
- ✅ Catégories et labels (emails, PDFs, analyses)
- ✅ Prompts LLM (demandes à l'IA)
- ✅ Messages d'erreur et résultats

---

## 📋 Résumé des changements de francisation

### 1️⃣ Email Classifier AI

**Catégories d'emails** (anciennes → nouvelles):
- `invoice` → `facture`
- `quote` → `devis`
- `complaint` → `reclamation`
- `spam` → `spam` (identique)
- `information` → `information` (identique)
- `other` → `autre`

**Prompts LLM**: Tous les prompts de classification, résumé et génération de réponse sont maintenant en français.

### 2️⃣ PDF Generator AI

**Types de documents** (anciennes → nouvelles):
- `quote` → `devis`
- `invoice` → `facture`
- `letter` → `lettre`
- `contract` → `contrat`
- `report` → `rapport`

**Noms de champs** (examples):
- `client_name` → `nom_client`
- `client_email` → `email_client`
- `amount` → `montant`
- `due_date` → `date_echéance`

**Prompts LLM**: Demandes de génération de contenu en français.

### 3️⃣ Excel Analyzer AI

**Types d'anomalies** (anciennes → nouvelles):
- `missing_values` → `valeurs_manquantes`
- `duplicates` → `doublons`
- `empty_column` → `colonne_vide`
- `high_missing_data` → `donnees_manquantes_excessives`

**Messages**: Tous les messages de suggestion et d'analyse sont en français.

---

## 🚀 Installation et démarrage

### Étape 1 : Cloner les app adaptées au français

Les apps sont déjà francisées. Aucun changement de code supplémentaire n'est nécessaire.

```bash
cd d:\DevPortable\Projects
```

### Étape 2 : Configuration Mistral (recommandé)

**Option A : Utiliser Mistral API (gratuit)**

1. Créer compte : https://console.mistral.ai
2. Obtenir clé API (gratuit : 3,600 requêtes/jour)
3. Configurer `.env` dans chaque app:

```bash
# Pour email-classifier-ai/.env
LLM_PROVIDER=mistral
MISTRAL_API_KEY=votre_cle_api_ici
JWT_SECRET_KEY=votre_secret_key

# Pour pdf-generator-ai/.env
LLM_PROVIDER=mistral
MISTRAL_API_KEY=votre_cle_api_ici
JWT_SECRET_KEY=votre_secret_key

# Pour excel-analyzer-ai/.env
LLM_PROVIDER=mistral
MISTRAL_API_KEY=votre_cle_api_ici
JWT_SECRET_KEY=votre_secret_key
```

**Option B : Utiliser Ollama (100% local gratuit)**

1. Installer Ollama : https://ollama.ai
2. Télécharger modèle : 
   ```bash
   ollama pull mistral
   # ou
   ollama pull neural-chat
   ```
3. Démarrer Ollama :
   ```bash
   ollama serve
   ```
4. Configurer `.env`:

```bash
# Dans chaque app/.env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
JWT_SECRET_KEY=votre_secret_key
```

---

## 🎯 Démarrage des apps

### App 1 : Email Classifier

```bash
cd email-classifier-ai

# Installer dépendances
pip install -r requirements.txt

# Configurer
cp .env.example .env
# Éditer .env avec vos paramètres Mistral ou Ollama

# Lancer
streamlit run app.py
```

**URL**: http://localhost:8501
**Demo**: `demo` / `demo123`

**Utilisation**:
1. Connectez-vous
2. Collez un email en français
3. Cliquez "Classifier"
4. L'app vous montre: Catégorie, Confiance, Résumé, Réponse suggérée

**Catégories affichées** (en français):
- 📄 Facture
- 💰 Devis
- 😞 Réclamation
- 🚫 Spam
- ℹ️ Information
- ❓ Autre

---

### App 2 : PDF Generator

```bash
cd pdf-generator-ai

# Installer dépendances
pip install -r requirements.txt

# Configurer
cp .env.example .env
# Éditer .env

# Lancer
streamlit run app.py --server.port 8502
```

**URL**: http://localhost:8502
**Demo**: `demo` / `demo123`

**Utilisation**:
1. Connectez-vous
2. Choisissez type de document:
   - 💼 **Devis** (professionnel)
   - 📋 **Facture** (paiement)
   - 📧 **Lettre** (commerciale)
   - 📄 **Contrat** (service)
   - 📊 **Rapport** (professionnel)
3. Remplissez les champs (en français)
4. Cliquez "Générer PDF"
5. Téléchargez le PDF généré

**Types de documents**:
- `devis` : Professionnel, présentation commerciale
- `facture` : Facturation, paiement
- `lettre` : Communication commerciale
- `contrat` : Accord légal simple
- `rapport` : Analyse et conclusions

---

### App 3 : Excel Analyzer

```bash
cd excel-analyzer-ai

# Installer dépendances
pip install -r requirements.txt

# Configurer
cp .env.example .env
# Éditer .env

# Lancer
streamlit run app.py --server.port 8503
```

**URL**: http://localhost:8503
**Demo**: `demo` / `demo123`

**Utilisation**:
1. Connectez-vous
2. Upload un fichier Excel/CSV
3. Attendez l'analyse (5-15 secondes)
4. Consultez les résultats en 4 onglets:
   - 📊 **Résumé**: Nombre lignes/colonnes, taille
   - ⚠️ **Anomalies**: Valeurs manquantes, doublons, colonnes vides
   - 📈 **Statistiques**: Min/max/moyenne/écart-type
   - 💡 **Suggestions**: Recommandations d'amélioration

**Types d'anomalies détectées**:
- `valeurs_manquantes`: Données manquantes (en %)
- `doublons`: Lignes en doublon
- `colonne_vide`: Colonnes complètement vides
- `donnees_manquantes_excessives`: >30% données manquantes

---

## 🔄 Basculer entre Mistral et Ollama

### Passer de Mistral à Ollama

```bash
# Dans .env de chaque app
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
```

### Passer de Ollama à Mistral

```bash
# Dans .env de chaque app
LLM_PROVIDER=mistral
MISTRAL_API_KEY=votre_cle_api
```

---

## 📝 Personnaliser les prompts LLM

### Email Classifier

Fichier: `email-classifier-ai/src/llm_service.py`

**Exemple de customisation** (Mistral Provider, ligne ~65):

```python
def classify_email(self, email_content: str) -> Dict[str, any]:
    """Classifier un email avec Mistral."""
    prompt = f"""Classifie l'email suivant dans UNE SEULE catégorie.
Catégories: facture, devis, reclamation, spam, information, autre

Email:
{email_content}

Réponds en JSON: {{"category": "...", "confidence": 0.0-1.0, "reason": "..."}}"""
```

**Pour ajouter une catégorie**:
1. Ajouter dans `VALID_CATEGORIES` (email_classifier.py)
2. Ajouter description dans `get_category_description()`
3. Ajouter dans le prompt du LLM

---

### PDF Generator

Fichier: `pdf-generator-ai/src/llm_service.py`

**Prompt de génération** (ligne ~52):

```python
prompt = f"""Génère un document {doc_type} professionnel avec les informations suivantes:

{fields_text}

Crée un contenu bien formaté et professionnel. Sois concis et courtois."""
```

---

### Excel Analyzer

Fichier: `excel-analyzer-ai/src/excel_analyzer.py`

Les suggestions sont générées statiquement (pas de LLM), donc faciles à customiser :

```python
# Ligne ~160
if len(df.columns) > 50:
    suggestions.append(f"Envisagez d'organiser {len(df.columns)} colonnes en plusieurs feuilles")
```

---

## 🧪 Tester que tout fonctionne en français

### Test rapide Email Classifier

```python
from email_classifier_ai.src.email_classifier import EmailClassifier

result = EmailClassifier.classify("""
Bonjour,

Veuillez trouver ci-joint la facture #INV-2025-001 pour un montant de 1500€.
Délai de paiement : 30 jours.

Cordialement
""")

print(result)
# Résultat attendu:
# {'category': 'facture', 'confidence': 0.95, 'reason': '...'}
```

### Test rapide PDF Generator

```python
from pdf_generator_ai.src.pdf_generator import PDFGenerator

fields = {
    "nom_client": "ACME SARL",
    "email_client": "contact@acme.com",
    "description": "Services consulting 2025",
    "montant": "2500€",
    "validite_jours": "30"
}

success, msg, path = PDFGenerator.generate_pdf("devis", fields)
print(f"✅ {msg}" if success else f"❌ {msg}")
```

### Test rapide Excel Analyzer

```python
from excel_analyzer_ai.src.excel_analyzer import ExcelAnalyzer
import pandas as pd

# Créer test data
df = pd.DataFrame({
    "nom": ["Alice", "Bob", None],
    "age": [25, 30, 35],
    "ville": ["Paris", "Lyon", "Marseille"]
})

anomalies = ExcelAnalyzer._detect_anomalies(df, "test")
print(anomalies)
# Résultat attendu:
# [{'type': 'valeurs_manquantes', 'column': 'nom', ...}]
```

---

## 🚀 Déployer avec Docker en français

Tous les Dockerfiles fonctionnent 100% en français.

```bash
# Email Classifier
docker-compose -f email-classifier-ai/docker-compose.yml up -d
# Accès: http://localhost:8501

# PDF Generator
docker-compose -f pdf-generator-ai/docker-compose.yml up -d
# Accès: http://localhost:8502

# Excel Analyzer
docker-compose -f excel-analyzer-ai/docker-compose.yml up -d
# Accès: http://localhost:8503
```

---

## 📚 Documentation supplémentaire

Chaque app a un **README.md complet** avec plus de détails:

- `email-classifier-ai/README.md` - Guide complet Email Classifier
- `pdf-generator-ai/README.md` - Guide complet PDF Generator
- `excel-analyzer-ai/README.md` - Guide complet Excel Analyzer
- `email-classifier-ai/docs/API.md` - Documentation API

---

## 🎓 Cas d'usage réels pour PMEs françaises

### Email Classifier → Vendre aux agences immo

```
Client: Agence immobilière parisienne
Problème: 100 emails/jour difficiles à trier
Solution: 
- Classifier auto (offre, réclamation, spam)
- Répondre auto aux offres
- Alerter sur réclamations urgentes
Temps gagné: 2h/jour → 30min/jour
Prix de vente: 100-200€/mois
```

### PDF Generator → Vendre aux petits cabinets

```
Client: Cabinet consultant
Problème: Génération manuelle de devis (30min-1h chacun)
Solution:
- Générer devis en 2 min
- Générer contrats en 2 min
- Templates personnalisés par client
Temps gagné: 5 devis/jour = 4h → 20min
Prix de vente: 150-300€/mois
```

### Excel Analyzer → Vendre aux PME données

```
Client: PME avec ventes/inventaire
Problème: Données sales mal organisées, anomalies non détectées
Solution:
- Upload fichier Excel
- Détection auto anomalies
- Suggestions amélioration
Temps gagné: 2-4h analyse → 10min
Prix de vente: 200-500€/mois
```

---

## ✅ Checklist démarrage

- [ ] Installer Python 3.11+
- [ ] Cloner les 3 apps
- [ ] Créer compte Mistral (ou installer Ollama)
- [ ] Configurer .env pour chaque app
- [ ] Installer requirements.txt
- [ ] Lancer les 3 apps
- [ ] Tester avec demo/demo123
- [ ] Vérifier réponses en français
- [ ] Adapter textes pour votre PME cible
- [ ] Déployer sur serveur

---

## 🆘 Dépannage

| Problème | Solution |
|----------|----------|
| "API key not found" | Vérifier .env et copier clé Mistral |
| "Ollama connection refused" | Lancer `ollama serve` |
| "Réponse en anglais" | Vérifier prompts LLM sont en français |
| "Database locked" | Supprimer `data/*.db` |
| "Port already in use" | Changer port Streamlit |

---

## 🎯 Prochaines étapes

1. **Customiser pour votre marché**
   - Adapter messages/prompts
   - Ajouter catégories spécifiques
   - Personnaliser templates

2. **Créer portfolio commercial**
   - 3 vidéos de démo
   - Pricing par PME
   - Package "Starter" / "Pro" / "Enterprise"

3. **Lancer MVP**
   - 3-5 clients pilotes
   - Recueillir feedback
   - Itérer rapidement

4. **Scaler**
   - Dashboard centralisé
   - Intégrations (Gmail, Slack, ERP)
   - Machine learning personnalisé

---

**Vous êtes prêt à monter votre startup d'IA pour PMEs! 🚀**

Besoin d'aide? Voir README.md dans chaque dossier app.
