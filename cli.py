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
    update_student
)

def menu():
    print("0.  Exit the Programm.")
    print("1.  Database: Add information to the Database.")
    print("2.  Student: List all the students.")
    print("3.  Student: Find student by id.")
    print("4.  Student: Delete student")
    print("5.  Student: Update Student's information.")
    print("6.  Lecturer: List all the lecturers.")
    print("7.  Lecturer: List all sessions a lecturer handles.")
    print("8.  Lecturer: Delete lecturer")
    print("9.  Lecturer: Update lecturer.")
    print("10. Session: The lecturer handling a particular session.")
    print("11. Session: Delete a session from the Database.")
    print("12. Session: List all the sessions in the Database.")
    print("13. Session: Update session information.")
    print("14. Studentsessions: View the sessions of a particular student.")
    print("15. Studentsessions: Views the students assigned to a particular session.")
    print("16. SchoolFees: Upload the student's school fees.")
    print("17. SchoolFees: View the school fees of a student.")
    print("18. SchoolFees: Update a student's fee")

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_programm()
        elif choice == "1":
            feed_database()
        elif choice == "2":
            list_all_students()
        elif choice == "3":
            find_student_by_id()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            list_all_lecturers()
        elif choice == "7":
            list_lecturers_sessions()
        elif choice == "8":
            delete_lecturer()
        elif choice == "9":
            update_lecturer()
        elif choice == "10":
            lecturer_of_session()
        elif choice == "11":
            delete_session()
        elif choice == "12":
            list_all_sessions()
        elif choice == "13":
            update_session()
        elif choice == "14":
            sessions_of_a_student()
        elif choice == "15":
            students_of_a_session()
        elif choice == "16":
            create_student_fees()
        elif choice == "17":
            student_school_fee()
        elif choice == "18":
            update_students_fee()
        else:
            print("Invalid choice! Select a valid choice.")


if __name__ == "__main__":
    main()


