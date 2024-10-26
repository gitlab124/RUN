import os
import subprocess
import time

# Chemin complet vers WIDFHost.exe dans le dossier WIDFHost de ProgramData
chemin_executable = os.path.join(os.environ['ProgramData'], 'WIDFHost', 'WIDFHost.exe')

# Attendre 30 secondes pour s'assurer que l'application est présente
time.sleep(30)

# Vérifie si le fichier existe et exécute-le
if os.path.isfile(chemin_executable):
    subprocess.run([chemin_executable])
else:
    print("L'application WIDFHost.exe est introuvable dans le dossier WIDFHost de ProgramData.")
