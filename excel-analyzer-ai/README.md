# 📊 Excel Analyzer AI

**Outil intelligent d'analyse et d'audit de fichiers Excel pour PME**

- ⚡ **Analyse instantanée** des données Excel/CSV
- 🔍 **Détection automatique d'anomalies** (données manquantes, doublons, etc.)
- 📈 **Graphiques interactifs** Plotly
- 💡 **Suggestions intelligentes** pour améliorer la qualité des données
- 🔐 **Multi-user avec authentification**
- 📦 **Historique complet** de toutes les analyses
- 🎯 **100% gratuit**

---

## 🎯 Vue d'ensemble

Excel Analyzer AI permet aux PME de :

1. **Upload des fichiers** Excel ou CSV
2. **Analyser automatiquement** la structure et la qualité
3. **Détecter les anomalies** (valeurs manquantes, doublons, etc.)
4. **Obtenir des suggestions** d'amélioration
5. **Conserver l'historique** de toutes les analyses

### Types d'anomalies détectées

- ❌ Valeurs manquantes (avec pourcentage)
- ❌ Lignes doublons
- ❌ Colonnes vides
- ❌ Données incohérentes
- ❌ Données aberrantes (outliers)

---

## 🚀 Installation rapide

```bash
cd excel-analyzer-ai

# Environnement Python
python -m venv venv
venv\Scripts\activate

# Dépendances
pip install -r requirements.txt

# Configuration
cp .env.example .env

# Lancer
streamlit run app.py
```

**URL** : http://localhost:8503
**Démo** : demo / demo123

---

## ⚙️ Configuration

```bash
# .env
LLM_PROVIDER=mistral
MISTRAL_API_KEY=votre_cle_ici

DB_TYPE=sqlite
DB_PATH=./data/excel_analyzer.db

JWT_SECRET_KEY=votre_secret
```

---

## 📖 Utilisation

### 1. Upload un fichier
- Cliquer sur "Upload un fichier Excel"
- Sélectionner un .xlsx, .xls ou .csv

### 2. Attendre l'analyse
- Parsing des données
- Détection d'anomalies
- Génération de suggestions

### 3. Consulter les résultats
- **Summary** : Nombre de lignes/colonnes, taille
- **Anomalies** : Problèmes détectés
- **Statistics** : Moyennes, écarts-types, min/max
- **Suggestions** : Recommandations d'amélioration

### 4. Accéder à l'historique
- Voir tous les fichiers analysés
- Réanaliser si nécessaire

---

## 🔧 Architecture

### Structure

```
excel-analyzer-ai/
├── app.py                  # Interface Streamlit
├── src/
│   ├── config.py          # Configuration
│   ├── logger.py          # Logging
│   ├── database.py        # BD SQLite
│   ├── auth.py            # Authentification
│   └── excel_analyzer.py  # Analyse (cœur)
├── database/
│   └── schema.sql         # Schéma BD
├── tests/                 # Tests
├── requirements.txt       # Dépendances
└── .env.example          # Configuration
```

### Modules clés

**ExcelAnalyzer.parse_file()** :
- Lit fichiers Excel/CSV
- Retourne DataFrames

**ExcelAnalyzer.analyze()** :
- Détecte anomalies
- Calcule statistiques
- Génère suggestions

**ExcelAnalyzer._detect_anomalies()** :
- Valeurs manquantes
- Doublons
- Colonnes vides
- Données excessives NULL

---

## 📊 Visualisations

- Graphiques Plotly interactifs
- Distribution des anomalies par sévérité
- Statistiques numériques
- Tableaux de données

---

## 🧪 Tests

```bash
pytest
pytest --cov=src --cov-report=html
pytest tests/test_excel_analyzer.py -v
```

---

## 🐛 Troubleshooting

### Erreur "Openpyxl not found"
```bash
pip install openpyxl
```

### Erreur "File too large"
- Augmenter `MAX_FILE_SIZE_MB` dans `.env`

### Erreur d'import Pandas
```bash
pip install pandas==2.1.3
```

---

## 🚀 Docker

```bash
docker-compose up -d
# http://localhost:8503
```

---

## 📄 License

MIT - Libre d'utilisation

---

**Analysez vos données maintenant :**
```bash
streamlit run app.py
```
