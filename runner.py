import os
import subprocess

chemin_executable = os.path.join(os.environ['ProgramData'], 'WIDFHost.exe')

if os.path.isfile(chemin_executable):
    subprocess.run([chemin_executable])
else:
    print("L'application WIDFHost.exe est introuvable dans ProgramData.")
