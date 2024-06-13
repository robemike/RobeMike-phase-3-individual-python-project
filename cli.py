from cli_functions import (
    exit_programm, 
    list_all_students,
    create_students,
    delete_student
)

def menu():
    print("0. Exit the Programm.")
    print("1. List all the students.")
    print("2. Add a new student.")
    print("3. Find student by id.")
    print("4. Delete student")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_programm()
        elif choice == "1":
            list_all_students()
        elif choice == "2":
            create_students()
        elif choice == "4":
            delete_student()
        else:
            print("Invalid choice! Select a valid choice.")


if __name__ == "__main__":
    main()

