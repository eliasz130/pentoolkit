# Imports/Defs to clean up program
import subprocess
import time
import sys

# Clears screen
def clear():
    subprocess.run("clear", shell=True)
    
# Run .py file/run install .sh file
def run(file):
    subprocess.run(file, shell=True)

# Run .sh file with arg
def run_script(script_path, *args):
    subprocess.run([script_path] + list(args))