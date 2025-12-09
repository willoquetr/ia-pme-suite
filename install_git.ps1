# Script d'installation Git pour Windows
# Ce script télécharge et configure Git

Write-Host "=== Installation de Git ===" -ForegroundColor Green

# Vérifier si Git existe déjà
try {
    $gitVersion = & "C:\Program Files\Git\cmd\git.exe" --version
    Write-Host "Git est déjà installé: $gitVersion" -ForegroundColor Green
    exit 0
} catch {
    Write-Host "Git pas trouvé, installation en cours..." -ForegroundColor Yellow
}

# Télécharger Git Portable
$gitUrl = "https://github.com/git-for-windows/git/releases/download/v2.43.0.windows.1/PortableGit-2.43.0-64-bit.7z.exe"
$gitPath = "D:\git-portable.exe"

Write-Host "Téléchargement de Git depuis $gitUrl..." -ForegroundColor Cyan
try {
    # Utiliser un client HTTP simple
    $webClient = New-Object System.Net.WebClient
    $webClient.DownloadFile($gitUrl, $gitPath)
    Write-Host "Téléchargement réussi!" -ForegroundColor Green
    
    # Exécuter l'installateur
    Write-Host "Installation en cours..." -ForegroundColor Cyan
    & $gitPath -y -o "D:\Git"
    
    Write-Host "Installation complète!" -ForegroundColor Green
    Write-Host "Git est prêt à être utilisé!" -ForegroundColor Green
    
    # Ajouter Git au PATH
    $env:Path += ";D:\Git\cmd"
    
} catch {
    Write-Host "Erreur d'installation: $_" -ForegroundColor Red
    Write-Host "Alternative: Installez Git manuellement depuis https://git-scm.com/download/win" -ForegroundColor Yellow
}
