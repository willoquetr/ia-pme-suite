# 🔌 API Documentation - Email Classifier AI

Cette documentation décrit comment intégrer Email Classifier AI avec d'autres systèmes.

## Vue d'ensemble

L'application expose plusieurs services Python qui peuvent être appelés directement :

### Services disponibles

1. **EmailClassifier** - Classification d'emails
2. **ResponseGenerator** - Génération de réponses et résumés
3. **AuthService** - Authentification utilisateurs
4. **Database** - Accès à la BD

---

## 📋 Service de Classification

### `EmailClassifier.classify(email_content: str)`

Classifier un email dans une catégorie.

**Paramètres** :
- `email_content` (str) : Contenu de l'email

**Retour** :
```python
{
    "category": "invoice",      # Catégorie détectée
    "confidence": 0.95,         # Confiance 0-1.0
    "reason": "Contains invoice details and amount"
}
```

**Exemple** :
```python
from src.email_classifier import EmailClassifier

result = EmailClassifier.classify("""
    Dear Client,
    Please find the attached invoice #12345 for $1000.
    Due date: 2025-01-15
""")

print(result)
# {'category': 'invoice', 'confidence': 0.95, 'reason': '...'}
```

### `EmailClassifier.get_categories()`

Obtenir la liste des catégories.

**Retour** :
```python
["invoice", "quote", "complaint", "spam", "information", "other"]
```

### `EmailClassifier.get_category_description(category: str)`

Obtenir la description d'une catégorie.

**Exemple** :
```python
EmailClassifier.get_category_description("invoice")
# "Factures et documents de facturation"
```

---

## 💬 Service de Génération

### `ResponseGenerator.generate(email_content, category, template="")`

Générer une réponse automatique.

**Paramètres** :
- `email_content` (str) : Contenu de l'email
- `category` (str) : Catégorie de l'email
- `template` (str, opt) : Template personnalisé

**Retour** :
```python
{
    "response": "Dear Client, Thank you for your inquiry...",
    "category": "invoice",
    "length": 245,
    "success": True
}
```

**Exemple** :
```python
from src.response_generator import ResponseGenerator

result = ResponseGenerator.generate(
    email_content="Can you send me the invoice?",
    category="invoice",
    template="Dear [CLIENT], your invoice is attached. Amount: [AMOUNT]"
)

print(result['response'])
```

### `ResponseGenerator.summarize(email_content: str)`

Résumer un email.

**Exemple** :
```python
summary = ResponseGenerator.summarize("""
    Dear Team,
    We need to discuss the Q1 budget. The finance department needs clarification.
    Please review and respond by Friday.
""")

print(summary)
# "Q1 budget discussion required. Finance team needs clarification. Response needed by Friday."
```

---

## 🔐 Service d'Authentification

### `AuthService.hash_password(password: str)`

Hasher un mot de passe.

```python
from src.auth import AuthService

hashed = AuthService.hash_password("my_password")
print(hashed)
# "5994471abb01112afcc18159f6cc74b4f511b99806da59b3caf5a9c173cacfc5"
```

### `AuthService.verify_password(password, hash_password)`

Vérifier un mot de passe.

```python
is_valid = AuthService.verify_password("my_password", hashed)
print(is_valid)  # True
```

### `AuthService.create_token(user_id, username)`

Créer un token JWT.

```python
token = AuthService.create_token(1, "john_doe")
print(token)
# "eyJ0eXAiOiJKV1QiLCJhbGc..."
```

### `AuthService.verify_token(token)`

Vérifier un token JWT.

```python
payload = AuthService.verify_token(token)
print(payload)
# {'user_id': 1, 'username': 'john_doe', 'exp': '2025-01-16T...'}
```

---

## 💾 Service de Base de Données

### Database connection

```python
from src.database import db

# La connexion est automatiquement initialisée
```

### `db.execute_query(query, params)`

Exécuter une requête SELECT.

```python
results = db.execute_query(
    "SELECT * FROM email_classifications WHERE user_id = ?",
    (1,)
)

for row in results:
    print(row['category'], row['confidence'])
```

### `db.execute_insert(query, params)`

Insérer une ligne.

```python
user_id = db.execute_insert(
    "INSERT INTO email_classifications (user_id, email_content, category, confidence) VALUES (?, ?, ?, ?)",
    (1, "email content", "invoice", 0.95)
)

print(f"ID inséré: {user_id}")
```

### `db.execute_update(query, params)`

Mettre à jour des lignes.

```python
affected = db.execute_update(
    "UPDATE email_classifications SET category = ? WHERE id = ?",
    ("quote", 5)
)

print(f"Lignes affectées: {affected}")
```

---

## 🧪 Exemples d'intégration

### Exemple 1 : Pipeline complet

```python
from src.email_classifier import EmailClassifier
from src.response_generator import ResponseGenerator
from src.database import db

# Email à traiter
email = """
Dear Support Team,
The product I received is broken. This is unacceptable!
Please send a replacement immediately.
"""

# 1. Classifier
classification = EmailClassifier.classify(email)

# 2. Résumer
summary = ResponseGenerator.summarize(email)

# 3. Générer réponse
response = ResponseGenerator.generate(
    email,
    classification['category']
)

# 4. Sauvegarder
db.execute_insert(
    """INSERT INTO email_classifications 
    (user_id, email_content, category, confidence, summary, generated_response)
    VALUES (?, ?, ?, ?, ?, ?)""",
    (
        1,
        email,
        classification['category'],
        classification['confidence'],
        summary,
        response['response']
    )
)

print(f"✅ Email classifié comme: {classification['category']}")
print(f"📄 Résumé: {summary}")
print(f"💬 Réponse: {response['response'][:100]}...")
```

### Exemple 2 : Batch processing

```python
import csv
from src.email_classifier import EmailClassifier
from src.database import db

# Lire fichier CSV
with open("emails.csv") as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # Classifier
        result = EmailClassifier.classify(row['content'])
        
        # Sauvegarder
        db.execute_insert(
            """INSERT INTO email_classifications 
            (user_id, email_content, category, confidence)
            VALUES (?, ?, ?, ?)""",
            (row['user_id'], row['content'], result['category'], result['confidence'])
        )

print("✅ Batch processing completed")
```

### Exemple 3 : Export rapports

```python
import json
from src.database import db

# Récupérer stats par catégorie
stats = db.execute_query("""
    SELECT category, COUNT(*) as count, AVG(confidence) as avg_confidence
    FROM email_classifications
    GROUP BY category
""")

# Exporter en JSON
report = {
    "total_emails": sum(s['count'] for s in stats),
    "by_category": stats
}

with open("report.json", "w") as f:
    json.dump(report, f, indent=2)

print(json.dumps(report, indent=2))
```

---

## 🔄 Intégration avec FastAPI (optionnel)

Pour exposer une API REST, créer `api.py` :

```python
from fastapi import FastAPI, HTTPException
from src.email_classifier import EmailClassifier
from src.response_generator import ResponseGenerator
from src.auth import AuthService

app = FastAPI(title="Email Classifier API")

@app.post("/api/classify")
def classify(email_content: str, token: str):
    """Classifier un email."""
    user = AuthService.verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    result = EmailClassifier.classify(email_content)
    return result

@app.post("/api/generate")
def generate(email_content: str, category: str, token: str):
    """Générer une réponse."""
    user = AuthService.verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    result = ResponseGenerator.generate(email_content, category)
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

Lancer :
```bash
pip install fastapi uvicorn
python api.py
```

---

## 📦 Utilisation en tant que package

Pour importer dans d'autres projets Python :

```bash
pip install -e /path/to/email-classifier-ai
```

Puis utiliser :
```python
from email_classifier_ai.src.email_classifier import EmailClassifier
from email_classifier_ai.src.response_generator import ResponseGenerator

# Utiliser les services
```

---

## ⚙️ Configuration pour l'intégration

Variables d'env à définir :
```bash
# LLM
LLM_PROVIDER=mistral
MISTRAL_API_KEY=...

# Database
DB_TYPE=sqlite
DB_PATH=./data/email_classifier.db

# Auth
JWT_SECRET_KEY=your_secret_key
```

---

## 🐛 Gestion des erreurs

Tous les services retournent des valeurs par défaut en cas d'erreur :

```python
# Classification échouée → category="other", confidence=0.3
# Génération échouée → response="Unable to generate..."
# BD échouée → exception levée (à attraper)
```

Exemple de gestion :

```python
try:
    result = EmailClassifier.classify(email)
except Exception as e:
    print(f"❌ Erreur de classification: {e}")
    result = {"category": "other", "confidence": 0.0}
```

---

## 📊 Schéma des données

### Table `email_classifications`
```sql
id                  | INTEGER (PK)
user_id             | INTEGER (FK)
email_content       | TEXT
category            | TEXT
confidence          | REAL
summary             | TEXT
generated_response  | TEXT
template_used       | TEXT
created_at          | TIMESTAMP
```

### Table `users`
```sql
id          | INTEGER (PK)
username    | TEXT (UNIQUE)
password_hash | TEXT
email       | TEXT (UNIQUE)
company_name | TEXT
is_admin    | BOOLEAN
created_at  | TIMESTAMP
updated_at  | TIMESTAMP
```

---

## 🚀 Performance

### Optimisations appliquées
- Index sur les colonnes fréquemment interrogées
- Requêtes paramétrées (prévention SQL injection)
- Caching des classifications (optionnel)

### Bench temps de réponse
- Classification : 0.5-2s (selon LLM)
- Résumé : 0.5-2s
- Génération réponse : 1-3s
- BD insert : <100ms

---

## 📄 License

MIT - Libre d'utilisation
