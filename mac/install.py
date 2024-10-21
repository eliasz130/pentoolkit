from imports import *

# Allows for install.sh to be run
def install_permissions():
    run("chmod +x mac/install.sh")

# Checks if Brew is installed
def is_brew_installed():
    try:
        subprocess.run(['brew', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

# Installs the apps needed with Brew
def install_app_with_brew():
    if is_brew_installed():
        try:
            install_permissions()
            run("mac/install.sh")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the install script: {e}")
    else:
        print("Homebrew is not installed. Please install Homebrew first. (Use https://github.com/Homebrew/brew/releases/download/4.4.1/Homebrew-4.4.1.pkg to quickly download it)")

# Runs install
if __name__ == "__main__":
    install_app_with_brew()
    clear()
    print("Installation complete.")
    run("mac/main.py")