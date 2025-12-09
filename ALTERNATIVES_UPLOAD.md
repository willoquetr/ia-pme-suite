# SOLUTION RAPIDE - Sans Git requis

## Si Git n'est pas installé, utilisez GitHub CLI (plus simple)

### Option 1: GitHub CLI (RECOMMANDÉ - 2 minutes)

```powershell
# 1. Installez GitHub CLI
choco install gh -y

# 2. Authentifiez-vous à GitHub
gh auth login

# 3. Créez le repo
gh repo create ia-pme-suite --public --source=. --remote=origin --push
```

---

## Option 2: Interface Web GitHub (sans ligne de commande)

1. **Créez le repo**
   - Allez sur: https://github.com/new
   - Remplissez les champs (voir GITHUB_ANSWER_IMAGE.md)
   - Cliquez "Create repository"

2. **Uploadez les fichiers via Web**
   - Dans votre nouveau repo, cliquez "Add file" → "Upload files"
   - Glissez-déposez ces fichiers depuis `D:\DevPortable\Projects\`:
     ```
     index.html
     LICENSE.md
     TERMS_OF_SERVICE.md
     CONTRIBUTING.md
     README_GITHUB.md (en tant que README.md)
     package.json
     .gitignore
     .github/SECURITY.md
     .github/CODEOWNERS
     ```

3. **Configurez GitHub Pages**
   - Settings → Pages
   - Source: Deploy from branch (main, /)
   - Enforce HTTPS: ✅
   - Attendez 2-3 minutes

---

## Option 3: Installer Git correctement

Si Chocolatey a échoué:

1. Téléchargez Git directement:
   ```
   https://git-scm.com/download/win
   ```

2. Exécutez l'installateur Windows

3. Redémarrez PowerShell ou CMD

4. Puis lancez:
   ```powershell
   cd D:\DevPortable\Projects
   git init
   git add .
   git commit -m "Initial: IA-PME Suite"
   git remote add origin https://github.com/willoquetr/ia-pme-suite.git
   git branch -M main
   git push -u origin main
   ```

---

## ✅ RÉSUMÉ

**La plus simple et rapide: Option 2 (Interface Web)**
- Aucun logiciel à installer
- Drag/drop des fichiers
- 5 minutes maximum

**La plus "pro": Option 1 (GitHub CLI)**
- Une seule commande: `gh repo create ia-pme-suite --public --source=. --remote=origin --push`
- Automatise tout
- Nécessite GitHub CLI (peut être installé via choco)

**La classique: Option 3 (Git)**
- Plus long (installation Git)
- Mais vous l'avez après pour d'autres projets

---

Quelle option préférez-vous?
