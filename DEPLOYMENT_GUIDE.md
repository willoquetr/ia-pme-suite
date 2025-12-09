# 🚀 Guide Déploiement Production - IA PME

## 📋 Checklist déploiement complet

---

## **PHASE 1: PRÉPARATION (Jour 1)**

### ☑️ Code & Config

- [ ] Tous les `.env.example` remplis correctement
- [ ] Variables sensibles en `.env` (jamais en repo)
- [ ] Tous les tests passent (pytest)
- [ ] Code en format Black (isort)
- [ ] Pas de hardcoded secrets
- [ ] Requirements.txt à jour

```bash
# Vérifier tests
cd email-classifier-ai && pytest && cd ..
cd pdf-generator-ai && pytest && cd ..
cd excel-analyzer-ai && pytest && cd ..

# Vérifier format
black .
isort .
```

### ☑️ Documentation

- [ ] README.md complète
- [ ] Installation guide fonctionnelle
- [ ] Architecture doc
- [ ] API documentation
- [ ] Troubleshooting guide

### ☑️ Security

- [ ] JWT secret key générée (min 32 chars)
- [ ] Database credentials sécurisées
- [ ] API keys en .env (jamais en code)
- [ ] Pas de données de test en prod
- [ ] HTTPS forcé (si web)

```bash
# Générer JWT secret
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## **PHASE 2: INFRASTRUCTURE (Jour 2)**

### Option A : Docker Compose local/server

```bash
# Vérifier Docker fonctionne
docker --version
docker-compose --version

# Build images
docker-compose -f email-classifier-ai/docker-compose.yml build
docker-compose -f pdf-generator-ai/docker-compose.yml build
docker-compose -f excel-analyzer-ai/docker-compose.yml build

# Lancer containers
docker-compose -f email-classifier-ai/docker-compose.yml up -d
docker-compose -f pdf-generator-ai/docker-compose.yml up -d
docker-compose -f excel-analyzer-ai/docker-compose.yml up -d

# Vérifier running
docker ps

# Logs
docker-compose logs -f
```

### Option B : Heroku (Gratuit avec limitations)

```bash
# 1. Installer Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# 2. Login
heroku login

# 3. Créer app
heroku create ia-pme-email
heroku create ia-pme-pdf
heroku create ia-pme-excel

# 4. Config variables
heroku config:set -a ia-pme-email LLM_PROVIDER=mistral
heroku config:set -a ia-pme-email MISTRAL_API_KEY=xxx

# 5. Deploy (Git)
git push heroku main

# 6. Logs
heroku logs --tail -a ia-pme-email
```

### Option C : Railway (RECOMMANDÉ - $5/mois)

```bash
# 1. Aller à https://railway.app/
# 2. Login avec GitHub
# 3. Create new project
# 4. Deploy GitHub repo
# 5. Ajouter variables d'env
# 6. Lancer deploy

# URL auto-générée : https://ia-pme-xxx.railway.app
```

### Option D : AWS / Google Cloud / Azure

Pour production serious:

```bash
# AWS Lightsail
# - EC2 instance t2.micro (gratuit 1 an)
# - Installer Docker
# - SSH deploy via docker-compose

# Google Cloud
# - Cloud Run (serverless)
# - App Engine
# - Compute Engine

# Azure
# - App Service
# - Container Instances
```

---

## **PHASE 3: DATABASE (Jour 3)**

### SQLite → Production Database

```bash
# Option 1: PostgreSQL local/hosted

# Installer PostgreSQL
# https://www.postgresql.org/download/

# Créer DB
psql -U postgres
CREATE DATABASE ia_pme;
CREATE USER ia_pme WITH PASSWORD 'STRONG_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE ia_pme TO ia_pme;

# Configurer .env
DB_TYPE=postgresql
DB_HOST=localhost
DB_NAME=ia_pme
DB_USER=ia_pme
DB_PASSWORD=STRONG_PASSWORD
```

### Option 2: Cloud Database

```bash
# Firebase Realtime DB (Google)
# - Gratuit jusqu'à 100 connections
# - https://firebase.google.com/

# MongoDB Atlas (Cloud)
# - Gratuit 512MB
# - https://www.mongodb.com/cloud/atlas

# Supabase (PostgreSQL managed)
# - Gratuit 500MB + auth
# - https://supabase.com/
```

### Migration données

```python
# Script migration SQLite → PostgreSQL
from src.database import db

# Exporter SQLite
data = db.execute_query("SELECT * FROM users")
classifications = db.execute_query("SELECT * FROM email_classifications")

# Importer PostgreSQL
for row in data:
    db.execute_insert("INSERT INTO users...", row)
```

---

## **PHASE 4: DÉPLOIEMENT APPS (Jour 4)**

### Streamlit Sharing (GRATUIT)

```bash
# 1. Repo GitHub public
# 2. Aller à https://share.streamlit.io/
# 3. "Deploy an app"
# 4. Sélectionner repo + fichier app.py
# 5. URL auto: https://ia-pme-email-xxx.streamlit.app

# Config app pour Streamlit
# ~/.streamlit/config.toml
[server]
maxUploadSize = 200
headless = true
```

### Custom Domain Streamlit

```bash
# Aller à Streamlit Cloud settings
# Ajouter custom domain
# Configurer DNS: CNAME → streamlit.io
# Attendre validation SSL (24h)
```

### Docker Swarm/Kubernetes (Avancé)

```bash
# Kubernetes deployment
kubectl apply -f email-classifier-k8s.yml
kubectl apply -f pdf-generator-k8s.yml
kubectl apply -f excel-analyzer-k8s.yml

# Check
kubectl get pods
kubectl logs pod-name
```

---

## **PHASE 5: DOMAINE & HTTPS (Jour 5)**

### Acheter domaine

```bash
# Providers:
# - Namecheap (bon marché)
# - GoDaddy
# - Google Domains
# - OVH (si français)

# Recommandation: iapme.fr ou ia-pme.fr
# Coût: 5-15€/an
```

### DNS Configuration

```bash
# Pour Streamlit Cloud:
# Ajouter CNAME: app.iapme.fr → xxx.streamlit.app

# Pour Heroku:
# Ajouter CNAME: app.iapme.fr → xxx.herokuapp.com

# Pour Railway/Custom:
# Ajouter A record: IP address de votre serveur
```

### SSL/HTTPS

```bash
# Let's Encrypt (GRATUIT)
sudo apt-get install certbot python3-certbot-nginx
sudo certbot certonly --nginx -d iapme.fr -d *.iapme.fr

# Auto-renew
sudo certbot renew --dry-run
```

---

## **PHASE 6: MONITORING & LOGGING (Jour 6)**

### Logs

```bash
# Fichiers logs
/var/log/ia-pme/

# Rotatation logs
logrotate /etc/logrotate.d/ia-pme

# Logs centralisés
# ELK Stack / Datadog / New Relic / Sentry
```

### Monitoring

```bash
# Server monitoring
uptime # Vérifier si app running
df -h  # Espace disque
free -h # RAM usage

# Application monitoring
# - Sentry pour errors
# - Datadog pour metrics
# - New Relic pour APM
```

### Alertes

```bash
# Quand app down:
# 1. Slack notification
# 2. Email alert
# 3. SMS alert (Twilio)

# Tools:
# - Healthchecks.io (gratuit)
# - Pingdom
# - Updown.io
```

---

## **PHASE 7: BACKUP & RECOVERY (Jour 7)**

### Backup database

```bash
# PostgreSQL backup
pg_dump -U ia_pme ia_pme > backup.sql

# Restore
psql -U ia_pme ia_pme < backup.sql

# Automated backups
0 2 * * * pg_dump -U ia_pme ia_pme > /backups/$(date +\%Y\%m\%d).sql
```

### Backup fichiers

```bash
# PDFs générés
tar -czf backups/pdfs_$(date +%Y%m%d).tar.gz data/pdfs/

# Configs
tar -czf backups/configs.tar.gz *.env

# Stockage cloud
# - AWS S3
# - Google Cloud Storage
# - Backblaze B2 (moins cher)
```

### Disaster recovery

```bash
# Procédure si crash:
1. Vérifier logs (docker logs / tail -f)
2. Redémarrer services (systemctl restart)
3. Restaurer DB backup
4. Restaurer fichiers backup
5. Test endpoints
6. Post-mortem
```

---

## **PHASE 8: TESTING PRODUCTION (Jour 8)**

### Load Testing

```bash
# Outils:
# - Apache Bench (ab)
# - Locust (Python)
# - JMeter

# Example Locust test
locust -f loadtest.py -u 100 -r 10
```

### Smoke tests

```python
# Test endpoints après deploy
import requests

def test_email_classifier():
    resp = requests.post(
        "https://ia-pme.com/api/classify",
        json={"email": "Test email"}
    )
    assert resp.status_code == 200

def test_pdf_generator():
    resp = requests.post(
        "https://ia-pme.com/api/pdf",
        json={"type": "devis", "fields": {...}}
    )
    assert resp.status_code == 200
```

### Security audit

```bash
# Dépendances vulnérables
pip audit

# Code scanning
bandit -r src/

# SSL test
curl -I https://ia-pme.com

# Headers sécurité
# - X-Frame-Options
# - X-Content-Type-Options
# - Strict-Transport-Security
```

---

## **PHASE 9: LAUNCH & COMMUNICATION (Jour 9)**

### Pre-launch

- [ ] Tester tous les endpoints
- [ ] Vérifier domaine fonctionne
- [ ] Test email notifications
- [ ] Test webhook integrations
- [ ] Vérifier landing page
- [ ] Vérifier pricing page

### Launch day

- [ ] Mettre landing page live
- [ ] Activer analytics
- [ ] Lancer première campagne emails
- [ ] Post sur social media
- [ ] Notifier early adopters
- [ ] Monitor error rates

### Post-launch

- [ ] Daily monitoring (1ère semaine)
- [ ] Collecte feedback
- [ ] Fix bugs urgents
- [ ] Optimiser performance
- [ ] Itérer features

---

## **CHECKLIST PRODUCTION**

```
INFRASTRUCTURE:
  ☑ Docker images prêtes
  ☑ Database configurée
  ☑ Backups automatiques
  ☑ Monitoring actif
  ☑ Alertes configurées

SÉCURITÉ:
  ☑ Secrets en .env
  ☑ Pas de hardcoded credentials
  ☑ SSL/HTTPS actif
  ☑ Security headers
  ☑ Rate limiting

PERFORMANCE:
  ☑ Load tested
  ☑ Caching configué
  ☑ CDN actif (si statique)
  ☑ Database optimisée
  ☑ <2s response time

MONITORING:
  ☑ Logs centralisés
  ☑ Error tracking
  ☑ Performance metrics
  ☑ Uptime monitoring
  ☑ Alertes configurées

DOCUMENTATION:
  ☑ Deployment guide
  ☑ Runbook (procédures)
  ☑ Incident response
  ☑ Architecture diagram
  ☑ API documentation
```

---

## 📊 Coûts estimés

| Composant | Option | Coût/mois |
|-----------|--------|-----------|
| Serveur | Heroku hobby | $7 |
| Serveur | Railway | $5-20 |
| Serveur | Lightsail | $3.50 |
| Database | Supabase free | $0 |
| Database | Supabase pro | $25 |
| Domain | Namecheap | $1-2/mois |
| Email | Brevo/Sendinblue | $0-20 |
| Monitoring | Sentry | $0-29 |
| CDN | Cloudflare | $0 |
| **TOTAL MIN** | | **$6-30/mois** |
| **TOTAL MID** | | **$50-100/mois** |

---

## 🎯 Timeline de déploiement

```
Week 1:
- Jour 1: Préparation code
- Jour 2: Infrastructure setup
- Jour 3: Database
- Jour 4: Déployer apps
- Jour 5: Domain + SSL

Week 2:
- Jour 6-7: Monitoring + Backups
- Jour 8: Testing
- Jour 9: Launch day
- Jour 10-14: Monitoring + Feedback

Total: 2 semaines pour production complète
```

---

## ✅ Status

**Prêt pour production**: ✅ OUI

Vous avez tous les fichiers de déploiement.
Suivez cette checklist et vous êtes en prod en 2 semaines maximum!

---

**Next**: Commencer par Option A (Docker Compose local) ou Option C (Railway) pour validation
