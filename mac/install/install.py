#!/usr/bin/env python3
import subprocess
import time

def clear():
    subprocess.run("clear", shell=True)

def run(file):
    # Make .sh file executable before running
    subprocess.run(f"chmod +x {file}", shell=True)
    subprocess.run(file, shell=True)

def is_brew_installed():
    try:
        subprocess.run(['brew', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def main_menu():
    while True:
        clear()
        print("Install Script")
        print("1. Install all")
        print("2. Install Nmap")
        print("3. Install Telnet")
        print("4. Install Rustscan (Faster Nmap)")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            run("mac/install/install/all.sh")
        elif choice == '2':
            clear()
            run("mac/install/install/nmap.sh")
        elif choice == '3':
            clear()
            run("mac/install/install/telnet.sh")
        elif choice == '4':
            clear()
            run("mac/install/install/rustscan.sh")
        elif choice == '5':
            clear()
            run("mac/main.py")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

def install_app_with_brew():
    if is_brew_installed():
        try:
            clear()
            main_menu()
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while running the install script: {e}")
    else:
        print("Homebrew is not installed. Please install Homebrew first.")

if __name__ == "__main__":
    clear()
    install_app_with_brew()