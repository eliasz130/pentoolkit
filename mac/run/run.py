#!/usr/bin/env python3
# imports (imports.py is not working for some reason on this file)
import subprocess
import time
this = False

# Clears screen
def clear():
    subprocess.run("clear", shell=True)
    
# Run .py file/run install .sh file
def run(file):
    subprocess.run(file, shell=True)

# Run .sh file with arg
def run_script(script_path, *args):
    subprocess.run([script_path] + list(args))

def main_menu():
    this = True
    while this == True:
        clear()
        print("Run Script")
        print("1. Run Nmap")
        print("2. Run Telnet")
        print("3. Run FTP")
        print("4. Run Rustscan (Faster Nmap)")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            scan_type = input("Enter the scan type (If any): ")
            options = input("Enter options (If any): ")
            target = input("Enter the target: ")
            run_script("mac/run/runlist/nmap.sh", "scan_type", "options", "target")
            nothing = input("Press enter to continue...")
        elif choice == '2':
            clear()
            target = input("Enter the target: ")
            port = input("Enter the port: ")
            run_script("mac/run/runlist/telnet.sh", "target", "port")
            nothing = input("Press enter to continue...")
        elif choice == '3':
            clear()
            options = input("Enter options (If any): ")
            user = input("Enter the user: ")
            host = input("Enter the host: ")
            userhost = user + "@" + host
            run_script("mac/run/runlist/ftp.sh", "options", "userhost")
            nothing = input("Press enter to continue...")
        elif choice == '4':
            clear()
            option = input("Enter options (if any): ")
            target = input("Enter the target: ")
            other = input("Enter other (if any): ")
            run_script("mac/run/runlist/rustscan.sh", "option", "target", "other")
            nothing = input("Press enter to continue...")
        elif choice == '5':
            clear()
            this = False
            run("mac/main.py")
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    clear()
    main_menu()