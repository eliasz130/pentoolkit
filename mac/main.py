#!/usr/bin/env python3
from imports import *

def check_programs():
    pass # Check to see if the Brew programs are installed takes off 1 from the main menu, as a backup for the install.py

def main_menu():
    while True:
        clear()
        print("Main Menu:")
        print("1. Run Script")
        print("2. Run Install Script")
        print("3. Run Update Script")
        print("4. Settings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            run("mac/run/run.py")
        elif choice == '2':
            clear()
            run("mac/install.py")
        elif choice == '3':
            clear()
            run("mac/update.py")
        elif choice == '4':
            clear()
            run("mac/settings.py")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    clear()
    main_menu()