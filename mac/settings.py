#!/usr/bin/env python3
from imports import *

def main_menu():
    options = {
        '1': "pass",
        '2': "pass",
        '3': "pass",
        '4': "pass",
        '5': "pass"
    }

    while True:
        clear()
        print("Settings")
        print("1. Auto Update")
        print("2.")
        print("3.")
        print("4.")
        print("5.")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice in options:
            clear()
            run(options[choice])
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)


if __name__ == "__main__":
    clear()
    main_menu()
