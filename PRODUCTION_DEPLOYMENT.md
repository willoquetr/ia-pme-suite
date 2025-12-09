# 🚀 DÉPLOIEMENT PRODUCTION - IA-PME Suite

**Objectif:** Avoir les 3 apps en ligne et accessibles (pas juste en local)  
**Coût:** €0-50/mois (options variées)  
**Durée:** 2-4 heures

---

## 🎯 **OPTIONS DE DÉPLOIEMENT**

### **Option 1: RAILWAY (RECOMMANDÉ) ⭐**

**Avantages:**
- ✅ Super facile
- ✅ Déploiement en 5 min
- ✅ Free tier: €5/mois de crédit
- ✅ Support 24/7
- ✅ Scalable

**Coût:** €0 (gratuit initialement), puis ~€10-30/mois en production

---

### **Option 2: HEROKU (Classic)**

**Avantages:**
- ✅ Très simple
- ✅ UI intuitive
- ✅ Auto-scaling

**Coût:** ~€7-50/mois (Eco plans)

**Important:** Heroku a retiré le free tier en 2022

---

### **Option 3: AWS (Scalable)**

**Avantages:**
- ✅ Très scalable
- ✅ Free tier 1 an

**Coût:** Gratuit 1 an (free tier), puis ~€20-100/mois

**Limitation:** Configuration plus complexe

---

## 🚀 **ÉTAPE 1: DÉPLOIEMENT RAILWAY** (Recommandé)

### Étape 1a: Créer un compte Railway

1. Allez sur: **https://railway.app**
2. Cliquez: **Get Started**
3. Login avec GitHub
4. Autorisez Railway à accéder vos repos

### Étape 1b: Déployer Email Classifier

1. Dans Railway, cliquez: **New Project**
2. Sélectionnez: **Deploy from GitHub repo**
3. Autorisez et sélectionnez: `ia-pme-suite` repo
4. Railway détecte automatiquement les Dockerfiles
5. Cliquez les 3 apps à déployer:
   - `email-classifier-ai`
   - `pdf-generator-ai`
   - `excel-analyzer-ai`

6. Pour chaque app, configurez les variables d'environnement:

   **Email Classifier:**
   ```
   MISTRAL_API_KEY=votre_clé_mistral
   DATABASE_URL=postgresql://...
   JWT_SECRET=votre_secret_aléatoire
   STREAMLIT_SERVER_HEADLESS=true
   ```

7. Cliquez: **Deploy**

8. Attendez 5-10 minutes

9. Obtenez l'URL publique (Railway génère automatiquement)

---

## 🐳 **ÉTAPE 2: PRÉPARER VOS APPS POUR PRODUCTION**

Les Dockerfiles existent déjà, mais mettez à jour les variables:

### Pour chaque app, créez `.env.production`:

**email-classifier-ai/.env.production:**
```
MISTRAL_API_KEY=sk-xxxxxxx
DATABASE_URL=postgresql://user:pass@host:5432/ia_pme_email
ENVIRONMENT=production
LOG_LEVEL=INFO
JWT_SECRET=your-secure-random-key-here
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_PORT=8501
```

**pdf-generator-ai/.env.production:**
```
MISTRAL_API_KEY=sk-xxxxxxx
DATABASE_URL=postgresql://user:pass@host:5432/ia_pme_pdf
ENVIRONMENT=production
LOG_LEVEL=INFO
JWT_SECRET=your-secure-random-key-here
```

**excel-analyzer-ai/.env.production:**
```
DATABASE_URL=postgresql://user:pass@host:5432/ia_pme_excel
ENVIRONMENT=production
LOG_LEVEL=INFO
```

---

## 📊 **ÉTAPE 3: CONFIGURER LA BASE DE DONNÉES**

### Option A: PostgreSQL chez Railway (Inclus)

1. Dans Railway, cliquez: **New Service**
2. Sélectionnez: **PostgreSQL**
3. Railway crée automatiquement la DB
4. Récupérez les credentials (COPY dans .env)

### Option B: PostgreSQL chez Vercel (Gratuit)

1. Allez sur: **https://vercel.com/storage/postgres**
2. Créez un projet
3. Récupérez les credentials

### Option C: Utiliser SQLite en production

**PAS RECOMMANDÉ** pour production avec plusieurs utilisateurs

---

## 🔐 **ÉTAPE 4: AJOUTER UN DOMAINE PERSONNALISÉ**

### Chez Railway:

1. Allez dans **Settings** de votre app
2. **Domains** → **Add Custom Domain**
3. Entrez: `email-classifier.ia-pme.fr`
4. Configurez CNAME chez Namecheap/OVH
5. Attendez 24-48h

---

## ✅ **CHECKLIST DÉPLOIEMENT PRODUCTION**

- [ ] Compte Railway créé
- [ ] 3 apps déployées
- [ ] Variables d'environnement configurées
- [ ] Base de données PostgreSQL créée
- [ ] SSL/HTTPS activé (auto chez Railway)
- [ ] Domaines personnalisés configurés
- [ ] Tests d'accès aux URLs publiques
- [ ] Email forwarder fonctionne
- [ ] Landing page pointe vers apps

---

## 📈 **APRÈS DÉPLOIEMENT**

### Vérifications:

1. Testez chaque app:
   ```
   https://email-classifier.ia-pme.fr
   https://pdf-generator.ia-pme.fr
   https://excel-analyzer.ia-pme.fr
   ```

2. Vérifiez login fonctionne (demo/demo123)

3. Testez avec fichiers réels:
   - Email Classifier: Envoyez un email test
   - PDF Generator: Générez un devis de test
   - Excel Analyzer: Uploadez un fichier Excel

4. Vérifiez que les bases de données reçoivent les données

---

## 💾 **MONITORING EN PRODUCTION**

### Chez Railway:

1. Dashboard → **Logs**
2. Surveillance temps réel des erreurs
3. Alertes automatiques si crash

### Recommandations:

- ✅ Configurez alertes email
- ✅ Monitoring quotidien
- ✅ Backups auto des données

---

## 🎯 **BUDGET PRODUCTION**

```
Railway (Email Classifier):    €2-5/mois
Railway (PDF Generator):       €2-5/mois
Railway (Excel Analyzer):      €2-5/mois
PostgreSQL Database:           €1-2/mois
Domaine (.fr):                €1.25/mois
Email (Zoho):                 €3/mois

TOTAL/MOIS:                   €11-20
TOTAL/AN:                     €132-240
```

**Très moins cher qu'un employé!** 💰

---

## 🚀 **ÉTAPES RAPIDES POUR DÉMARRER AUJOURD'HUI**

```bash
# 1. Créez compte Railway
# 2. Connectez votre GitHub
# 3. Importez ia-pme-suite repo
# 4. Railway détecte automatiquement Dockerfiles
# 5. Cliquez Deploy pour chaque app
# 6. Configurez variables d'env
# 7. Attendez 10 minutes
# 8. Apps en ligne! 🎉
```

---

**Vous êtes maintenant prêt pour production! 🚀**

© 2025 IA-PME
