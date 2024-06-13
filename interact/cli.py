from cli_functions import (
    exit_programm
)

def menu():
    print("0. Exit the Programm.")
    print("1. List all the students.")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_programm()

if __name__ == "__main__":
    main()

