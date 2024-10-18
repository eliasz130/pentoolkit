import subprocess
import platform
import sys

def install_permissions():
    subprocess.run("chmod +x mac/install.sh", shell=True)

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
            subprocess.run("mac/install.sh", shell=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the install script: {e}")
    else:
        print("Homebrew is not installed. Please install Homebrew first. (Use https://github.com/Homebrew/brew/releases/download/4.4.1/Homebrew-4.4.1.pkg to quickly download it)")

if __name__ == "__main__":
    if platform.system() != "Darwin":
        print("This script can only be run on macOS.")
        sys.exit(1)
    install_permissions()
    install_app_with_brew()
    subprocess.run("clear", shell=True)
    print("Installation complete.")
    print("Press any key to go to the main menu.")
    input()
    subprocess.run("mac/main.py", shell=True)