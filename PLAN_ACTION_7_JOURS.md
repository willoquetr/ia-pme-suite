# ⚡ PLAN D'ACTION 7 JOURS

**Objectif:** Être prêt à prospécter la semaine prochaine  
**Temps requis:** 1-2h/jour pendant 7 jours  
**Résultat:** Infrastructure complète + 1er client en 14 jours

---

## 📋 **SEMAINE 1 (7-13 décembre)**

### **JOUR 1 (Aujourd'hui) - DOMAINE & EMAIL**

**Temps:** 30 min

#### Tâche 1: Acheter domaine
```
1. Allez sur: https://www.namecheap.com
2. Cherchez: ia-pme.fr
3. Cliquez: Add to cart
4. Remplissez infos: Rudy Willoquet
5. Paiement: ~€12-15
6. ✅ Domaine acheté

Temps: 10 min
```

#### Tâche 2: Créer email professionnel
```
1. Allez sur: https://www.zoho.com/mail
2. Sign Up
3. Email: rudy@ia-pme.fr
4. Password: [sécurisé]
5. Organisation: IA-PME
6. ✅ Compte créé

Temps: 10 min
```

#### Tâche 3: Configurer DNS
```
1. Chez Namecheap: Manage Domain → Nameservers
2. Zoho vous donne les records
3. Copy-paste les MX records
4. Sauvegardez
5. ✅ DNS en attente (24-48h)

Temps: 10 min
```

**Checkpoint:** Domaine acheté + Zoho Account created + DNS configuré ✅

---

### **JOUR 2 (8 décembre) - REPOSITORY GITHUB FINAL**

**Temps:** 30 min

#### Tâche 1: Vérifier landing page en ligne
```
1. Allez sur: https://ia-pme-suite.github.io
2. Vérifiez que c'est en ligne
3. Cliquez sur "Demander une démo"
4. Vérifiez que ça ouvre email
5. ✅ Landing page fonctionne

Temps: 5 min
```

#### Tâche 2: Finaliser repo GitHub
```
1. Vérifiez que tous les fichiers sont uploadés:
   ✅ index.html
   ✅ LICENSE.md
   ✅ TERMS_OF_SERVICE.md
   ✅ CONTRIBUTING.md
   ✅ .gitignore
   ✅ .github/SECURITY.md
   ✅ .github/CODEOWNERS
   ✅ .github/pull_request_template.md

Temps: 10 min
```

#### Tâche 3: Pointer domaine vers GitHub Pages
```
1. Repo → Settings → Pages
2. Custom domain: ia-pme.fr
3. Cliquez Save
4. GitHub crée CNAME file
5. Attendez 24h pour propagation
6. ✅ ia-pme.fr pointera vers landing page

Temps: 5 min
```

#### Tâche 4: Vérifier HTTPS
```
1. Attendez 5-10 minutes
2. Settings → Pages
3. Cochez: Enforce HTTPS
4. Save
5. ✅ HTTPS activé

Temps: 5 min
```

**Checkpoint:** Landing page pointera vers ia-pme.fr avec HTTPS ✅

---

### **JOUR 3 (9 décembre) - CRÉATION CALENDLY**

**Temps:** 20 min

#### Tâche 1: Créer compte Calendly
```
1. Allez sur: https://calendly.com (gratuit)
2. Sign up avec email perso
3. Créez un event type:
   Nom: "Démo IA-PME"
   Durée: 15 minutes
   Description: "Découvrez comment automatiser vos tâches"
4. ✅ Event créé

Temps: 10 min
```

#### Tâche 2: Personnaliser disponibilités
```
1. Définissez votre timezone
2. Heures disponibles:
   Lundi-Vendredi: 10h-17h
   Samedi: 10h-12h
3. Buffer après chaque démo: 15 min
4. ✅ Calendrier configuré

Temps: 10 min
```

#### Tâche 3: Récupérer votre lien
```
1. Copiez votre lien public Calendly
   Ex: calendly.com/rudy/demo-ia-pme
2. Gardez-le pour prospection
3. ✅ Lien prêt

Temps: pas de temps
```

**Checkpoint:** Calendly en ligne et prêt pour démos ✅

---

### **JOUR 4 (10 décembre) - DÉPLOIEMENT PRODUCTION**

**Temps:** 2-3 heures

#### Tâche 1: Créer compte Railway
```
1. Allez sur: https://railway.app
2. Sign up avec GitHub
3. Autorisez Railway
4. ✅ Compte créé

Temps: 5 min
```

#### Tâche 2: Déployer Email Classifier
```
1. Railway: New Project
2. Sélectionnez: ia-pme-suite repo
3. Choisissez: email-classifier-ai
4. Configurez variables d'env:
   MISTRAL_API_KEY=sk-xxx
   DATABASE_URL=postgresql://...
   JWT_SECRET=random-key
5. Deploy
6. Attendez 5-10 minutes
7. ✅ Email Classifier en ligne!

Temps: 15 min + 10 min attente
```

#### Tâche 3: Déployer PDF Generator
```
Répétez Tâche 2 pour:
pdf-generator-ai

Temps: 15 min + 10 min attente
```

#### Tâche 4: Déployer Excel Analyzer
```
Répétez Tâche 2 pour:
excel-analyzer-ai

Temps: 15 min + 10 min attente
```

#### Tâche 5: Tester accès
```
1. Railway vous donne 3 URLs:
   https://email-classifier-xxx.railway.app
   https://pdf-generator-xxx.railway.app
   https://excel-analyzer-xxx.railway.app

2. Testez chaque app:
   - Ouvre sans erreur?
   - Login marche (demo/demo123)?
   - Peut générer quelque chose?

3. ✅ Les 3 apps en production!

Temps: 10 min
```

**Checkpoint:** 3 apps déployées en production ✅

---

### **JOUR 5-6 (11-12 décembre) - PROSPECTION SETUP**

**Temps:** 1 heure

#### Tâche 1: Lister 50 PMEs cibles
```
Utilisez:
1. Google Maps: "plombier rohan", "expert-comptable vannes", etc.
2. Pages Jaunes: pagesjaunes.fr
3. Chambre Commerce: morbihan.cci.fr
4. LinkedIn: recherche par région

Créez un spreadsheet:
Nom | Email | Téléphone | Secteur | Notes

Cible: 50 entreprises

Temps: 45 min
```

#### Tâche 2: Rédiger email de prospection
```
Utilisez templates dans: PROSPECTION_BRETAGNE.md

Créez 3 versions selon secteur:
1. Immobilier
2. Artisans/BTP
3. Consulting/Services

Temps: 15 min
```

**Checkpoint:** 50 prospects identifiés + emails rédigés ✅

---

### **JOUR 7 (13 décembre) - LANCEMENT PROSPECTION**

**Temps:** 1-2 heures

#### Tâche 1: Envoyer 1er batch emails
```
1. Envoyez à 10 entreprises jour 1
2. Sujet: [Rohan] Gagnez 20h/mois sur vos [tâches]
3. Body: Email template personalisé
4. Include: Lien Calendly + email contact
5. Suivez les réponses

Temps: 30 min
```

#### Tâche 2: Visites directes (optionnel mais recommandé)
```
1. Allez visiter 2-3 agences immobilières/artisans
2. "Je fais un tour des entreprises locales"
3. Montrez rapidement votre démo (3 min)
4. Laissez un flyer + email
5. Proposez un RDV suivi

Temps: 1-2h
```

#### Tâche 3: Suivi des contacts
```
1. Notez qui a répondu
2. Programmez RDVs dans Calendly
3. Préparez démo pour demain
4. Confirmez via email

Temps: 30 min
```

**Checkpoint:** Prospection lancée + premiers contacts! ✅

---

## 📊 **CHECKLIST COMPLÈTE 7 JOURS**

### **Jour 1**
- [ ] Domaine .fr acheté (ia-pme.fr)
- [ ] Zoho Mail account créé (rudy@ia-pme.fr)
- [ ] DNS records configurés
- [ ] En attente propagation (24-48h)

### **Jour 2**
- [ ] Landing page vérifiée
- [ ] GitHub repo finalisé
- [ ] Domaine pointe GitHub Pages
- [ ] HTTPS activé (en attente)

### **Jour 3**
- [ ] Calendly créé
- [ ] Démos disponibilités configurées
- [ ] Lien public copié

### **Jour 4**
- [ ] Railway account créé
- [ ] Email Classifier déployée ✅
- [ ] PDF Generator déployée ✅
- [ ] Excel Analyzer déployée ✅
- [ ] Les 3 apps testées et fonctionnelles

### **Jour 5-6**
- [ ] 50 PMEs identifiées
- [ ] Spreadsheet créée
- [ ] Emails de prospection rédigés (3 versions)
- [ ] Lien Calendly intégré aux emails

### **Jour 7**
- [ ] 1er batch (10) emails envoyés
- [ ] 2-3 visites directes (optionnel)
- [ ] 1ers contacts réceptifs identifiés
- [ ] RDVs programmés dans Calendly

---

## 🎯 **RÉSULTATS ATTENDUS À J+7**

```
✅ Infrastructure complète
✅ Landing page en ligne (ia-pme.fr)
✅ 3 apps déployées en production
✅ Email professionnel fonctionne
✅ Prospection lancée
✅ 3-5 démos programmées
✅ 1-2 clients potentiels chauds

À partir de là: demande démo → 15 min zoom → signature contrat

Délai avant 1er client: 10-14 jours TOTAL
```

---

## 💡 **TIPS PENDANT LA SEMAINE**

### **Pour l'email Zoho**
- Attendez que les DNS se propagent (24-48h)
- Si ça marche pas, attendez plus avant de paniquer
- Alternative: Forwarder gratuit vers Gmail en 5 min

### **Pour Railway**
- Les apps peuvent prendre 10-15 min à démarrer
- C'est normal, soyez patient
- Vérifiez les logs si ça fonctionne pas

### **Pour la prospection**
- Les PME répondent plus lentement (48h-3 jours)
- Les appels directs ont 50%+ de taux réussite
- Vendredi après-midi: mauvais moment pour contacter
- Lundi-jeudi 10h-12h: meilleur timing

### **Pour Calendly**
- Mettez des créneaux réels et disponibles
- 15 min c'est perfect pour démo
- Envoyez un rappel 24h avant

---

## 🚀 **APRÈS CES 7 JOURS**

```
SEMAINE 2:
- Prospection accélérée
- 20-30 emails/jour
- Démos 2-3/jour
- Suivi relances

SEMAINE 3:
- 1er client signature
- 1er paiement reçu
- Momentum établi
- Expansion Bretagne commence

JANVIER:
- 5-10 clients
- Revenu: €245-1,500/mois
- Business lancé! 🎉
```

---

## ❓ **SI VOUS ÊTES BLOQUÉ**

**Domaine:** support@namecheap.com  
**Email:** support@zoho.com  
**Deploy:** support@railway.app  
**GitHub Pages:** github.com/support  

---

**Vous avez TOUT ce qu'il faut. Lancez-vous! 🚀**

À vous de jouer maintenant!

© 2025 IA-PME
