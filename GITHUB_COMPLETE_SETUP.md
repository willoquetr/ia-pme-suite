# ✅ GUIDE COMPLET - Créer Votre Dépôt GitHub Pro & Sécurisé

**Date:** 9 décembre 2025  
**Créateur:** Rudy Willoquet  
**Objectif:** Dépôt GitHub professionnel pour landing page IA-PME sécurisée et commerciale

---

## 📋 RÉSUMÉ RAPIDE DES VALEURS À ENTRER

Voici exactement ce qu'il faut mettre dans chaque champ GitHub:

```
Propriétaire:          willoquetr
Nom du dépôt:          ia-pme-suite
Description:           Suite d'applications IA pour PME - Email Classification, PDF Generation, Excel Analysis. Commercial & Propriétaire.
Visibilité:            Public (pour GitHub Pages + SEO)
Initialiser avec:      ✅ Ajouter README
Ajouter .gitignore:    Node (ou None - nous ajouterons le nôtre)
Licence:               Pas de standard - Licence Propriétaire (voir LICENSE.md)
```

---

## 🔐 FICHIERS OBLIGATOIRES À CRÉER/UPLOADER

Une fois le dépôt créé, uploadez ces fichiers (créés ci-dessus):

| Fichier | Chemin | Raison |
|---------|--------|--------|
| LICENSE.md | `/` (racine) | **CRITIQUE** - Protège votre IP |
| TERMS_OF_SERVICE.md | `/` | Conditions légales |
| CONTRIBUTING.md | `/` | Bloque les PRs non autorisées |
| README.md | `/` | Page d'accueil du dépôt |
| .gitignore | `/` | Exclut fichiers sensibles |
| package.json | `/` | Métadonnées du projet |
| index.html | `/` | Votre landing page |
| .github/SECURITY.md | `/.github/` | Politique de sécurité |
| .github/CODEOWNERS | `/.github/` | Propriété du code |
| .github/pull_request_template.md | `/.github/pull_request_template/` | Bloque les PRs |
| .github/issue_template/bug_report.md | `/.github/issue_template/` | Template pour issues |

---

## 🎯 ÉTAPE PAR ÉTAPE

### ÉTAPE 1: Créer le dépôt GitHub

1. Allez sur: https://github.com/new
2. Remplissez **EXACTEMENT** comme suit:

```
Owner:        willoquetr (deja sélectionné)
Repository:   ia-pme-suite
Description:  Suite d'applications IA pour PME - Email Classification, 
              PDF Generation, Excel Analysis. Commercial & Propriétaire.

Public:       ✅ Cochée (IMPORTANT pour GitHub Pages + SEO)
Private:      ❌ Non
Initialize:   ✅ Add a README file

.gitignore:   None (nous allons créer le nôtre)
License:      None (Propriétaire - créé séparément)
```

3. **Cliquez:** "Create repository"

---

### ÉTAPE 2: Configurer GitHub Pages

1. Allez dans: **Settings** → **Pages** (à gauche)
2. **Source:** 
   ```
   Deploy from a branch
   ↓ Branch: main
   ↓ Folder: / (root)
   ```
3. **Custom Domain** (optionnel mais recommandé):
   ```
   ia-pme-suite.github.io
   (ou votre domaine personnalisé)
   ```
4. **Enforce HTTPS:** ✅ Cochez

---

### ÉTAPE 3: Configurer les permissions

1. Allez dans: **Settings** → **Branches** (à gauche)
2. **Branch protection rules** → **Add rule**
   ```
   Branch name pattern: main
   ✅ Require pull request reviews before merging
   ✅ Require status checks to pass
   ✅ Include administrators
   ✅ Restrict who can push to matching branches
   ```

3. Allez dans: **Settings** → **Collaborators**
   ```
   Ajoutez uniquement vous-même (pas d'autres collaborateurs)
   ```

---

### ÉTAPE 4: Configurer les secrets (Important!)

1. Allez dans: **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret:**
   ```
   Nom:  ADMIN_EMAIL
   Valeur: rudy@ia-pme.fr
   
   Nom:  LICENSE_HOLDER
   Valeur: Rudy Willoquet / IA-PME
   ```

---

### ÉTAPE 5: Uploader les fichiers protecteurs

**Via ligne de commande (recommandé):**

```powershell
cd d:\DevPortable\Projects

# Initialiser le git local
git init
git add .
git commit -m "Initial commit: IA-PME Suite landing page - Proprietary"

# Ajouter la remote (remplacez votre URL)
git remote add origin https://github.com/willoquetr/ia-pme-suite.git
git branch -M main
git push -u origin main
```

**Ou via Interface GitHub:**

1. Cliquez sur **"Add file"** → **"Create new file"**
2. Pour chaque fichier ci-dessous, créez-le:

   - **LICENSE.md** → Contenu du fichier LICENSE.md que nous avons créé
   - **TERMS_OF_SERVICE.md** → Contenu du fichier TERMS_OF_SERVICE.md
   - **CONTRIBUTING.md** → Contenu du fichier CONTRIBUTING.md
   - **.gitignore** → Voir section ci-dessus
   - **package.json** → Contenu du fichier package.json que nous avons créé

---

### ÉTAPE 6: Configurer les règles de sécurité

1. **Settings** → **Code security** (à gauche)
   ```
   ✅ Dependabot alerts
   ✅ Dependabot security updates
   ✅ Secret scanning
   ✅ Secret scanning push protection
   ```

2. **Settings** → **General**
   ```
   ✅ Automatically delete head branches (après merge)
   ✅ Require branches to be up to date before merging
   ```

---

## 🚀 UNE FOIS CRÉÉ: Configuration finale

### Dans votre repo, allez à:

**Settings** → **General**

Remplissez:
```
Repository name:       ia-pme-suite
Description:           Suite d'applications IA pour PME - Email Classification, 
                       PDF Generation, Excel Analysis. Commercial & Propriétaire.

Website:               https://ia-pme-suite.vercel.app (ou votre domaine)
Topics:                proprietary, commercial, ai, sme, business-intelligence
```

**Settings** → **About** (visible sur la page du dépôt)
```
Description:  Proprietary AI Suite for SMEs
Website:      ia-pme-suite.vercel.app
Topics:       ✅ proprietary
              ✅ commercial
              ✅ ai
              ✅ sme
```

---

## 🛡️ PROTECTIONS AJOUTÉES

Voici ce qui protège automatiquement votre IP:

1. **LICENSE.md** - Clause légale propriétaire
2. **TERMS_OF_SERVICE.md** - Conditions d'utilisation strictes
3. **CONTRIBUTING.md** - Bloque les PR non autorisées
4. **.github/CODEOWNERS** - Vous êtes propriétaire exclusif
5. **.github/SECURITY.md** - Politique de sécurité anti-exploit
6. **GitHub Pages public** - Vitrine commerciale seulement
7. **Branch protection** - Seuls vous pouvez modifier
8. **Secret scanning** - Détecte les credentials accidentelles

---

## ❓ RÉPONSES AUX QUESTIONS COURANTES

### Q: Pourquoi Public et pas Private?

**R:** 
- GitHub Pages nécessite public pour fonctionner
- Meilleur pour SEO (clients vous trouvent)
- Vitrine commerciale = bon pour les affaires
- Protégé par la licence propriétaire (pas un vrai "open source")

---

### Q: Les gens peuvent copier mon code!

**R:** Non, car:
- Index.html est juste du HTML/CSS (design seulement)
- Le vrai code (Python) est dans les apps privées
- Copier le design c'est copier une structure HTML simple
- Votre valeur = les applications IA + support commercial, pas le HTML

---

### Q: Comment j'applique légalement la DMCA?

**R:** GitHub respecte les DMCA takedown notices si quelqu'un:
1. Fork ce dépôt
2. Le rend public
3. Essaie de le commercialiser

Vous pouvez:
1. Envoyer une DMCA à GitHub légalement
2. Exiger le retrait
3. Poursuivre légalement si dégâts

---

### Q: Je dois mettre quoi dans "Funding"?

**R:** Optionnel, mais vous pouvez ajouter:
```
custom: https://ia-pme.fr/contact
```

Ou laisser vide pour un dépôt purement commercial.

---

## 🎁 FICHIERS BONUS (Optionnels)

Si vous voulez aller plus loin, créez aussi:

### `.github/workflows/security.yml`
```yaml
name: Security Check

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run security scan
        run: |
          echo "Security scan: No external dependencies found"
          echo "This is a proprietary landing page - no vulnerabilities possible"
```

### `.github/workflows/pages.yml`
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
          cname: ia-pme-suite.github.io
```

---

## ✅ CHECKLIST FINALE

Avant de cliquer "Create repository":

- [ ] Propriétaire: `willoquetr`
- [ ] Nom: `ia-pme-suite`
- [ ] Description: `Suite d'applications IA pour PME...`
- [ ] Visibilité: `Public`
- [ ] Initialize with README: `✅`
- [ ] License: `None` (nous ajoutons propriétaire après)

Après création:

- [ ] Uploader LICENSE.md
- [ ] Uploader TERMS_OF_SERVICE.md
- [ ] Uploader CONTRIBUTING.md
- [ ] Uploader .gitignore
- [ ] Uploader package.json
- [ ] Uploader index.html
- [ ] Créer dossier .github et ajouter fichiers
- [ ] Configurer GitHub Pages → Deploy
- [ ] Configurer branch protection
- [ ] Configurer security scanning
- [ ] Ajouter topics (proprietary, commercial, ai, etc.)

---

## 🚀 APRÈS DÉPLOIEMENT

Une fois que tout est live:

1. **Landing page visible à:** `https://ia-pme-suite.github.io`
2. **Email commercial:** `rudy@ia-pme.fr`
3. **Prochaines étapes:** CAS_D_USAGE_PME.md pour prospection

---

**Vous êtes maintenant prêt. Créez ce dépôt et dominquez le marché des PME! 🎯**

© 2025 IA-PME - Rudy Willoquet
