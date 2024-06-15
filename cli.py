from cli_functions import (
    exit_programm, 
    list_all_students,
    create_students,
    find_student_by_id,
    delete_student,
    create_lecturers,
    list_all_lecturers,
    list_lecturers_sessions,
    create_session,
    lecturer_of_session,
    delete_session,
    list_all_sessions,
    update_session,
    create_students_sessions,
    sessions_of_a_student,
    students_of_a_session,
    create_student_fees
)

def menu():
    print("0.  Exit the Programm.")
    print("1.  Student: List all the students.")
    print("2.  Student: Add a new student.")
    print("3.  Student: Find student by id.")
    print("4.  Student: Delete student")
    print("5.  Lecturer: Add lecturer to Program")
    print("6.  Lecturer: List all the lecturers.")
    print("7.  Lecturer: List all sessions a lecturer teaches")
    print("8.  Session: Add session to Program")
    print("9.  Session: The lecturer teaching a particular session.")
    print("10. Session: Delete a session from the Database.")
    print("11. Session: List all the sessions in the Database.")
    print("12. Session: Update session information.")
    print("13. Studentsessions: Add the student's and session's foreign keys.")
    print("14. Studentsessions: sessions of a particular student.")
    print("15. Studentsessions: Students of a particular session.")
    print("16. Add Student's school fees.")

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
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            create_lecturers()
        elif choice == "6":
            list_all_lecturers()
        elif choice == "7":
            list_lecturers_sessions()
        elif choice == "8":
            create_session()
        elif choice == "9":
            lecturer_of_session()
        elif choice == "10":
            delete_session()
        elif choice == "11":
            list_all_sessions()
        elif choice == "12":
            update_session()
        elif choice == "13":
            create_students_sessions()
        elif choice == "14":
            sessions_of_a_student()
        elif choice == "15":
            students_of_a_session()
        elif choice == "16":
            create_student_fees()
        else:
            print("Invalid choice! Select a valid choice.")


if __name__ == "__main__":
    main()


