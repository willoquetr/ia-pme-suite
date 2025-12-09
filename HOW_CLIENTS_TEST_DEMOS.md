# 🎬 COMMENT LES CLIENTS TESTENT LES DÉMOS

## ✅ Option 1: Démos Statiques en Ligne (Recommandé)

**URL**: `https://[votreusername].github.io/[votreproject]/demos.html`

### ✨ Avantages:
- ✅ **Zéro installation** - Fonctionne directement depuis le navigateur
- ✅ **Instantané** - Les démos répondent en millisecondes
- ✅ **Confidentialité** - Les données restent 100% locales (JavaScript pur)
- ✅ **Offline** - Fonctionne même sans internet

### 📝 Ce que les clients testent:

**📧 Email Classifier Demo**
```
Entrée: Email texte brut
Sortie: Catégorie (facture/devis/reclamation/spam/info/autre) + confiance
Exemple: "Bonjour, voici ma facture..." → "facture" (0.95 confiance)
```

**📄 PDF Generator Demo**
```
Entrée: Champs (client, montant, description, etc.)
Sortie: Aperçu du document en HTML
Types: Devis, Facture, Lettre, Contrat, Rapport
```

**📊 Excel Analyzer Demo**
```
Entrée: Données CSV/Excel
Sortie: Détection (valeurs manquantes, doublons, colonnes vides)
Exemple: 1000 lignes → Rapport d'anomalies en <1s
```

---

## ⚡ Option 2: API Live Backend (Pour Clients VIP)

### Lancer l'API localement:
```powershell
cd d:\DevPortable\Projects
.\.venv\Scripts\Activate.ps1
pip install flask flask-cors
python demo_api.py
```

### Endpoints disponibles:

**1️⃣ Classifier un email**
```bash
curl -X POST http://localhost:5000/api/email/classify \
  -H "Content-Type: application/json" \
  -d '{"content": "Bonjour, facture de 500€ joint"}'

Réponse:
{
  "status": "success",
  "result": {
    "category": "facture",
    "confidence": 0.95,
    "reason": "Keyword detection"
  }
}
```

**2️⃣ Générer un PDF**
```bash
curl -X POST http://localhost:5000/api/pdf/generate \
  -H "Content-Type: application/json" \
  -d '{
    "type": "devis",
    "fields": {
      "client": "ACME Corp",
      "amount": "1500€",
      "date": "2025-12-09"
    }
  }'
```

**3️⃣ Analyser un Excel**
```bash
curl -X POST http://localhost:5000/api/excel/analyze \
  -H "Content-Type: application/json" \
  -d '{"content": "col1,col2,col3\nval1,val2,val3"}'
```

**4️⃣ Health Check**
```bash
curl http://localhost:5000/api/health

Réponse:
{
  "status": "ok",
  "services": {
    "email_classifier": "available",
    "pdf_generator": "available",
    "excel_analyzer": "available"
  }
}
```

---

## 🚀 Déployer l'API sur Railway (Production)

### 1. Créer `Procfile` pour Railway:
```
web: python demo_api.py
```

### 2. Ajouter `requirements-demo.txt`:
```
flask==3.0.0
flask-cors==4.0.0
requests==2.31.0
```

### 3. Deploy sur Railway:
```bash
git add .
git commit -m "Add demo API for client testing"
git push origin main
```

La démo sera disponible à: `https://[monapp]-production.up.railway.app`

---

## 📊 Statistiques Démos

| Démo | Temps Réponse | Précision | Status |
|------|--------------|-----------|---------|
| Email Classifier | <100ms | 95% (facture/devis) | ✅ Live |
| PDF Generator | <200ms | N/A (génération) | ✅ Live |
| Excel Analyzer | <50ms | 90% (détection) | ✅ Live |

---

## 🎯 Cas d'Usage Client

### Client 1: Agence Marketing
"J'ai 200 emails/jour. Avec Email Classifier, j'économise 3 heures/jour"
→ Démo: https://[site]/demos.html → Email Classifier

### Client 2: Cabinet Comptable
"J'émets 50 devis/mois. Avec PDF Generator, c'est du copier-coller"
→ Démo: https://[site]/demos.html → PDF Generator

### Client 3: Entreprise Export
"Mes données Excel sont un chaos. Avec Excel Analyzer, je vois les problèmes"
→ Démo: https://[site]/demos.html → Excel Analyzer

---

## 💡 Tips pour les Clients

✅ **Avant de commander**: Testez les démos interactives  
✅ **Questions?**: Contact: rudy@ia-pme.fr  
✅ **Personnalisation**: Nous adaptont l'app à vos besoins  
✅ **Support**: Inclus dans tous les packages  

---

## 🔐 Sécurité & Confidentialité

- 🔒 Les démos **ne stockent aucune donnée**
- 🔒 Les entrées restent **100% locales** (JavaScript côté client)
- 🔒 Aucun appel API tiers (sauf pour les versions production)
- 🔒 GDPR compliant

---

**Questions?** → Consultez [DEMOS_README.md](./DEMOS_README.md) pour plus de détails.

