# Imports/Defs to clean up program
import subprocess
import time
import sys

def clear():
    subprocess.run("clear", shell=True)
    
def run(file):
    subprocess.run(file, shell=True)