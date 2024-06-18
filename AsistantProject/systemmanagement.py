import subprocess
from respond import respond

def increase_volume():
    subprocess.run(["osascript", "-e", 'set volume output volume (output volume of (get volume settings) + 10)'])
    respond("Audio level increased")

def decrease_volume():
    subprocess.run(["osascript", "-e", 'set volume output volume (output volume of (get volume settings) - 10)'])
    respond("Audio level decreased")
