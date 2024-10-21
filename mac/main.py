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

        # Runs scripts
        if choice == '1':
            clear()
            run("mac/run/run.py")
        # Installs scripts
        elif choice == '2':
            clear()
            run("mac/install.py")
        # Updates scripts
        elif choice == '3':
            clear()
            run("mac/update.py")
        # Settings
        elif choice == '4':
            clear()
            run("mac/settings.py")
        # Exits program
        elif choice == '5':
            print("Exiting...")
            break
        # Invalid choice
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

# Runs menu
if __name__ == "__main__":
    clear()
    main_menu()