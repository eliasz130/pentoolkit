#!/usr/bin/env python3
import subprocess
import time

def clear():
    subprocess.run("clear", shell=True)

def run(file):
    subprocess.run(f"chmod +x {file} && {file}", shell=True)

def is_brew_installed():
    return subprocess.run(['brew', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0

def main_menu():
    options = {
        '1': "mac/install/install/all.sh",
        '2': "mac/install/install/nmap.sh",
        '3': "mac/install/install/telnet.sh",
        '4': "mac/install/install/rustscan.sh",
        '5': "mac/main.py"
    }
    while True:
        clear()
        print("Install Script")
        print("1. Install all")
        print("2. Install Nmap")
        print("3. Install Telnet")
        print("4. Install Rustscan (Faster Nmap)")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice in options:
            clear()
            run(options[choice])
            if choice == '5':
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
