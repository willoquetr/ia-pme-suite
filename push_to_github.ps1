#!/usr/bin/env powershell

<#
.SYNOPSIS
    Script pour pousser votre IA-PME Suite vers GitHub
    
.DESCRIPTION
    Initialise le repo Git local et pousse vers GitHub
    
.EXAMPLE
    powershell -ExecutionPolicy Bypass -File push_to_github.ps1
#>

param(
    [string]$GitHubUrl = "https://github.com/willoquetr/ia-pme-suite.git",
    [string]$UserName = "Rudy Willoquet",
    [string]$Email = "rudy@ia-pme.fr",
    [string]$ProjectPath = "D:\DevPortable\Projects"
)

# Couleurs
$Green = @{ ForegroundColor = "Green" }
$Red = @{ ForegroundColor = "Red" }
$Yellow = @{ ForegroundColor = "Yellow" }
$Cyan = @{ ForegroundColor = "Cyan" }

# En-tête
Write-Host @Green "
╔════════════════════════════════════════════════════════════════╗
║         IA-PME SUITE - PUSH VERS GITHUB                      ║
║                                                                ║
║  Script d'upload sécurisé de votre landing page propriétaire  ║
╚════════════════════════════════════════════════════════════════╝
"

# Vérifier que le dossier existe
if (-not (Test-Path $ProjectPath)) {
    Write-Host @Red "❌ ERREUR: Dossier $ProjectPath non trouvé"
    exit 1
}

# Vérifier que index.html existe
if (-not (Test-Path "$ProjectPath\index.html")) {
    Write-Host @Red "❌ ERREUR: index.html non trouvé dans $ProjectPath"
    exit 1
}

# Aller au dossier du projet
Set-Location $ProjectPath
Write-Host @Cyan "📁 Localisation: $(Get-Location)"

# Vérifier Git
Write-Host @Yellow "`n[0/7] Vérification de Git..."
try {
    $gitVersion = & git --version 2>&1
    Write-Host @Green "✅ Git trouvé: $gitVersion"
} catch {
    Write-Host @Red "❌ ERREUR: Git n'est pas installé ou n'est pas dans le PATH"
    Write-Host @Yellow "   Installez Git depuis: https://git-scm.com/download/win"
    exit 1
}

# Configuration Git
Write-Host @Yellow "`n[1/7] Configuration Git..."
& git config --global user.name $UserName
& git config --global user.email $Email
Write-Host @Green "✅ Git configuré pour: $UserName <$Email>"

# Initialisation
Write-Host @Yellow "`n[2/7] Initialisation du repo local..."
if (Test-Path ".git") {
    Write-Host @Cyan "   (Repo existant trouvé, réinitialisation...)"
    Remove-Item -Recurse -Force .git
}
& git init
Write-Host @Green "✅ Repo initialisé"

# Ajouter les fichiers
Write-Host @Yellow "`n[3/7] Ajout des fichiers..."
& git add .
$fileCount = & git ls-files | Measure-Object -Line | Select-Object -ExpandProperty Lines
Write-Host @Green "✅ $fileCount fichiers ajoutés"

# Afficher les fichiers ajoutés
Write-Host @Cyan "`n   Fichiers à uploader:"
& git ls-files | ForEach-Object { Write-Host "   • $_" }

# Commit
Write-Host @Yellow "`n[4/7] Création du commit..."
& git commit -m "Initial commit: IA-PME Suite landing page - Proprietary"
Write-Host @Green "✅ Commit créé"

# Ajouter la remote
Write-Host @Yellow "`n[5/7] Ajout de la remote GitHub..."
& git remote remove origin 2>$null
& git remote add origin $GitHubUrl
Write-Host @Green "✅ Remote ajoutée: $GitHubUrl"

# Branche
Write-Host @Yellow "`n[6/7] Configuration de la branche..."
& git branch -M main
Write-Host @Green "✅ Branche: main"

# Pause avant push
Write-Host @Yellow "`n[7/7] PRÊT POUR LE PUSH"
Write-Host @Cyan "
┌────────────────────────────────────────────────────────────────┐
│ AVANT DE CONTINUER - CRÉEZ LE REPO GITHUB                     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│ 1. Allez sur: https://github.com/new                          │
│                                                                │
│ 2. Remplissez:                                                │
│    • Propriétaire: willoquetr                                 │
│    • Nom: ia-pme-suite                                        │
│    • Description: Suite d'applications IA pour PME...         │
│    • Visibilité: Public                                       │
│    • Initialize: ❌ NON (README ne pas ajouter)              │
│    • .gitignore: None                                         │
│    • License: None                                            │
│                                                                │
│ 3. Cliquez: \"Create repository\"                              │
│                                                                │
│ 4. Revenez ici et appuyez sur une touche pour pousser         │
│                                                                │
└────────────────────────────────────────────────────────────────┘
"

Write-Host -NoNewline "Appuyez sur une touche quand le repo GitHub est créé..."
[void][System.Console]::ReadKey($true)

# Push
Write-Host @Cyan "`n🚀 Envoi vers GitHub..."
try {
    & git push -u origin main --force
    Write-Host @Green "✅ Push réussi!"
} catch {
    Write-Host @Red "❌ ERREUR lors du push: $_"
    Write-Host @Yellow "   Assurez-vous que:"
    Write-Host @Yellow "   • Le repo GitHub existe"
    Write-Host @Yellow "   • Vous avez les permissions d'accès"
    Write-Host @Yellow "   • Vous êtes connecté à GitHub via HTTPS ou SSH"
    exit 1
}

# Afficher le résumé
Write-Host @Green "
╔════════════════════════════════════════════════════════════════╗
║                      ✅ SUCCÈS!                               ║
╚════════════════════════════════════════════════════════════════╝
"

Write-Host @Cyan "Votre repo est maintenant sur GitHub:"
Write-Host @Green "📍 https://github.com/willoquetr/ia-pme-suite"

Write-Host @Yellow "`n📋 PROCHAINES ÉTAPES:"
Write-Host @Cyan "
1. Allez sur: https://github.com/willoquetr/ia-pme-suite/settings/pages
   
2. Configurez GitHub Pages:
   • Source: Deploy from a branch
   • Branch: main
   • Folder: / (root)
   
3. Activez HTTPS:
   • Cochez: \"Enforce HTTPS\"
   
4. Attendez 2-3 minutes...
   
5. Votre landing page sera accessible à:
   📱 https://ia-pme-suite.github.io
"

Write-Host @Green "
Votre dépôt est maintenant:
✅ Créé et initié
✅ Protégé par LICENSE.md propriétaire
✅ Bloqué pour les fork commerciaux
✅ Prêt pour GitHub Pages
"

Write-Host -NoNewline "Appuyez sur une touche pour terminer..."
[void][System.Console]::ReadKey($true)
