import os
import subprocess

def clear():
    subprocess.run("clear", shell=True)
    
def run_permissions():
    subprocess.run("chmod +x mac/install.py", shell=True)
    
    
def check_programs():
    pass # Check to see if the Brew programs are installed takes off 1 from the main menu, as a backup for the install.py

def main_menu():
    while True:
        print("Main Menu:")
        print("1. Run Script")
        print("2. Run Install Script")
        print("3. Run Update Script")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            
        elif choice == '2':
            clear()
            subprocess.run("mac/install.py", shell=True)
        elif choice == '3':
            subprocess.run("mac/update.py", shell=True)
            clear()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    run_permissions()
    clear()
    main_menu()