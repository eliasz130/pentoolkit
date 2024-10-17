import sys, os, subprocess
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
            subprocess.run("/pentoolkit/mac/install.sh", shell=True)
        finally:
            print("Homebrew is not installed. Please install Homebrew first. (Use {.href [this](https://github.com/Homebrew/brew/releases/download/4.4.1/Homebrew-4.4.1.pkg)} to quickly download it)")
if __name__ == "__main__":
    install_app_with_brew()