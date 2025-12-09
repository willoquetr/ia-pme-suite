@echo off
REM Script Windows pour initialiser et pousser votre repo GitHub
REM Instructions:
REM 1. Changez YOUR_USERNAME et YOUR_EMAIL ci-dessous
REM 2. Changez YOUR_GITHUB_URL avec l'URL de votre repo
REM 3. Exécutez ce script

echo ================================================
echo PREPARATION DU DEPOT GITHUB
echo ================================================

cd /d "D:\DevPortable\Projects"

REM Vérifier que nous sommes au bon endroit
if not exist "index.html" (
    echo ERREUR: index.html non trouvé
    echo Assurez-vous de lancer depuis D:\DevPortable\Projects
    pause
    exit /b 1
)

echo.
echo [1/6] Configuration Git...
git config --global user.name "Rudy Willoquet"
git config --global user.email "rudy@ia-pme.fr"

echo.
echo [2/6] Initialisation du dépôt local...
git init

echo.
echo [3/6] Ajout de tous les fichiers...
git add .

echo.
echo [4/6] Premier commit...
git commit -m "Initial commit: IA-PME Suite landing page - Proprietary"

echo.
echo [5/6] Ajout de la remote GitHub...
REM CHANGE CECI AVEC VOTRE URL DE REPO
git remote add origin https://github.com/willoquetr/ia-pme-suite.git

echo.
echo [6/6] Renommage de la branche...
git branch -M main

echo.
echo ================================================
echo PRET A POUSSER?
echo ================================================
echo.
echo Avant de continuer:
echo 1. Allez sur https://github.com/new
echo 2. Créez un nouveau repo "ia-pme-suite"
echo 3. Ne sélectionnez PAS "Initialize with README"
echo 4. Cliquez "Create repository"
echo 5. Revenez ici et appuyez sur une touche
echo.
pause

echo.
echo Envoi vers GitHub...
git push -u origin main

echo.
echo ================================================
echo SUCCES!
echo ================================================
echo.
echo Votre repo est maintenant sur GitHub:
echo https://github.com/willoquetr/ia-pme-suite
echo.
echo Prochaine étape:
echo 1. Settings -> Pages
echo 2. Source: Deploy from branch (main, /)
echo 3. Attendez 2 minutes
echo 4. Accédez à: https://ia-pme-suite.github.io
echo.
pause
