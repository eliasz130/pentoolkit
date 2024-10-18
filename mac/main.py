import os
import subprocess

def run_install():
    subprocess.run("mac/install.py", shell=True)

def check_programs():
    pass # Check to see if the Brew programs are installed takes off 1 from the main menu, as a backup for the install.py

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Run Install Script")
        print("2. ")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            run_install()
        elif choice == '2':
            pass
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()