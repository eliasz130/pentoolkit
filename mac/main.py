import os
import subprocess

def install_permissions():
    subprocess.run("chmod +x mac/run.sh", shell=True)
    
def check_programs():
    pass # Check to see if the Brew programs are installed takes off 1 from the main menu, as a backup for the install.py

def main_menu():
    while True:
        subprocess.run("clear", shell=True)
        print("Main Menu:")
        print("1. Run Script")
        print("2. Run Install Script")
        print("3. Run Update Script")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            subprocess.run("clear", shell=True)
            subprocess.run("mac/run.sh", shell=True)
        elif choice == '2':
            subprocess.run("clear", shell=True)
            subprocess.run("mac/install.py", shell=True)
        elif choice == '3':
            subprocess.run("clear", shell=True)
            subprocess.run("mac/update.py", shell=True)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    subprocess.run("clear", shell=True)
    main_menu()