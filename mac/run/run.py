#!/usr/bin/env python3
from imports import *
def main_menu():
    while True:
        clear()
        print("Run Script")
        print("1. Run Nmap")
        print("2. Run Wireshark")
        print("3. Run Bettercap")
        print("4. Run John The Ripper")
        print("5. Back")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            run("mac/run/runlist/nmap.sh")
        elif choice == '2':
            clear()
            run("mac/run/runlist/wireshark.sh")
        elif choice == '3':
            clear()
            run("mac/run/runlist/bettercap.sh")
        elif choice == '4':
            clear()
            run("mac/run/runlist/john.sh")
        elif choice == '5':
            clear()
            run("mac/main.py")
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    clear()
    main_menu()