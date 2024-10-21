#!/usr/bin/env python3
from imports import *

def main_menu():
    while True:
        clear()
        print("Run Script")
        print("1. Run Nmap")
        print("2. Run Bettercap")
        print("3. Run John The Ripper")
        print("4. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            scan_type = input("Enter the scan type: ")
            options = input("Enter options: ")
            target = input("Enter the target: ")
            run_script("mac/run/nmap.sh", "scan_type", "options", "target")
        elif choice == '2':
            clear()
            run_script("mac/run/bettercap.sh", "arg1", "arg2")
        elif choice == '3':
            clear()
            run_script("mac/run/john.sh", "arg1", "arg2")
        elif choice == '4':
            clear()
            run("mac/main.py")
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    clear()
    main_menu()