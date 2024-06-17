from cli_functions import (
    exit_programm, 
    list_all_students,
    find_student_by_id,
    delete_student,
    feed_database,
    list_all_lecturers,
    list_lecturers_sessions,
    lecturer_of_session,
    delete_session,
    list_all_sessions,
    update_session,
    sessions_of_a_student,
    students_of_a_session,
    create_student_fees,
    student_school_fee,
    delete_lecturer,
    update_students_fee,
    update_lecturer,
    update_student,
    create_lecturer,
    create_sessions,
    create_student,
    create_students_sessions
)

def menu():
    print("0.  Exit the Programm.")
    print("1.  Database: Add information to the Database.")
    print("2.  Student: Add a student to the programm.")
    print("3.  Student: List all the students.")
    print("4.  Student: Find student by id.")
    print("5.  Student: Delete student")
    print("6.  Student: Update Student's information.")
    print("7.  Lecturer: Add a lecturer to the programm.")
    print("8.  Lecturer: List all the lecturers.")
    print("9.  Lecturer: List all sessions a lecturer handles.")
    print("10. Lecturer: Delete lecturer")
    print("11. Lecturer: Update lecturer.")
    print("12. Session: Add a session to the programm")
    print("13. Session: The lecturer handling a particular session.")
    print("14. Session: Delete a session from the Database.")
    print("15. Session: List all the sessions in the Database.")
    print("16. Session: Update session information.")
    print("17. Studentsessions: Add a student's and related session's id.")
    print("18. Studentsessions: View the sessions of a particular student.")
    print("19. Studentsessions: Views the students assigned to a particular session.")
    print("20. SchoolFees: Upload the student's school fees.")
    print("21. SchoolFees: View the school fees of a student.")
    print("22. SchoolFees: Update a student's fee")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_programm()
        elif choice == "1":
            feed_database()
        elif choice == "2":
            create_student()
        elif choice == "3":
            list_all_students()
        elif choice == "4":
            find_student_by_id()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            update_student()
        elif choice == "7":
            create_lecturer()
        elif choice == "8":
            list_all_lecturers()
        elif choice == "9":
            list_lecturers_sessions()
        elif choice == "10":
            delete_lecturer()
        elif choice == "11":
            update_lecturer()
        elif choice == "12":
            create_sessions()
        elif choice == "13":
            lecturer_of_session()
        elif choice == "14":
            delete_session()
        elif choice == "15":
            list_all_sessions()
        elif choice == "16":
            update_session()
        elif choice == "17":
            create_students_sessions()
        elif choice == "18":
            sessions_of_a_student()
        elif choice == "19":
            students_of_a_session()
        elif choice == "20":
            create_student_fees()
        elif choice == "21":
            student_school_fee()
        elif choice == "22":
            update_students_fee()
        else:
            print("Invalid choice! Select a valid choice.")


if __name__ == "__main__":
    main()


