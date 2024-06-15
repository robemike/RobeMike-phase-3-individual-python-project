from cli_functions import (
    exit_programm, 
    list_all_students,
    create_students,
    delete_student,
    create_teachers,
    create_subject,
    list_all_teachers,
    list_teachers_subjects,
    teacher_of_subject,
    delete_subject,
    list_all_subjects,
    update_subject
)

def menu():
    print("0. Exit the Programm.")
    print("1. List all the students.")
    print("2. Add a new student.")
    print("3. Find student by id.")
    print("4. Delete student")
    print("5. Add Teacher to Program")
    print("6. Add subject to Program")
    print("7. List all the teachers.")
    print("8. List all subjects a teacher teaches")
    print("9. The teacher teaching a particular subject.")
    print("10. Delete a subject from the Database.")
    print("11. List all the Subjects in the Database.")
    print("12. Update subject information.")

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
        elif choice == "5":
            create_teachers()
        elif choice == "6":
            create_subject()
        elif choice == "7":
            list_all_teachers()
        elif choice == "8":
            list_teachers_subjects()
        elif choice == "9":
            teacher_of_subject()
        elif choice == "10":
            delete_subject()
        elif choice == "11":
            list_all_subjects()
        elif choice == "12":
            update_subject()
        else:
            print("Invalid choice! Select a valid choice.")


if __name__ == "__main__":
    main()


