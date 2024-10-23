#!/usr/bin/env python3
from imports import *

def main_menu():
    while True:
        clear()
        print("Settings")
        print("1. Auto Update")
        print("2. ")
        print("3. ")
        print("4. ")
        print("5. ")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear()
            pass
        elif choice == '2':
            clear()
            pass
        elif choice == '3':
            clear()
            pass
        elif choice == '4':
            clear()
            pass
        elif choice == '5':
            clear()
            pass
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    clear()
    main_menu()