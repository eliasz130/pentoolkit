#!/usr/bin/env python3
from imports import *

def install_permissions():
    run("chmod +x mac/install.sh")

def is_brew_installed():
    """Check if Homebrew is installed"""
    try:
        subprocess.run(['brew', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def install_app_with_brew():
    """Install an app using Homebrew"""
    if is_brew_installed():
        try:
            install_permissions()
            run("mac/install.sh")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the install script: {e}")
    else:
        print("Homebrew is not installed. Please install Homebrew first. (Use https://github.com/Homebrew/brew/releases/download/4.4.1/Homebrew-4.4.1.pkg to quickly download it)")

if __name__ == "__main__":
    install_app_with_brew()
    clear()
    print("Installation complete.")
    run("mac/main.py")