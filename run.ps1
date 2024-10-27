# Chemin complet vers WINKey.vbs dans le dossier WIDFHost de ProgramData
$chemin_executable = Join-Path $env:ProgramData 'WIDFHost\WINKey.vbs'

# Attendre 30 secondes pour s'assurer que l'application est présente
Start-Sleep -Seconds 4

# Vérifie si le fichier existe et exécute-le
if (Test-Path $chemin_executable) {
    # Exécuter le fichier VBS en utilisant cscript
    & 'C:\Windows\System32\cscript.exe' $chemin_executable
} else {
    Write-Host "Le script WINKey.vbs est introuvable dans le dossier WIDFHost de ProgramData."
}
