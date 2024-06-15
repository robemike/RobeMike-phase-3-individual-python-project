from cli_functions import (
    exit_programm, 
    list_all_students,
    create_students,
    delete_student,
    create_teachers,
    list_all_teachers,
    list_teachers_subjects,
    create_subject,
    teacher_of_subject,
    delete_subject,
    list_all_subjects,
    update_subject,
    create_student_subjects,
    subjects_of_a_student,
    students_of_a_subject
)

def menu():
    print("0.  Exit the Programm.")
    print("1.  Student: List all the students.")
    print("2.  Student: Add a new student.")
    print("3.  Student: Find student by id.")
    print("4.  Student: Delete student")
    print("5.  Teacher: Add Teacher to Program")
    print("6.  Teacher: List all the teachers.")
    print("7.  Teacher: List all subjects a teacher teaches")
    print("8.  Subject: Add subject to Program")
    print("9.  Subject: The teacher teaching a particular subject.")
    print("10. Subject: Delete a subject from the Database.")
    print("11. Subject: List all the Subjects in the Database.")
    print("12. Subject: Update subject information.")
    print("13. StudentSubjects: Add the student's and subject's foreign keys.")
    print("14. StudentSubjects: Subjects of a particular student.")
    print("15. StudentSubjects: Students of a particular subject.")

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
            pass
        elif choice == "4":
            delete_student()
        elif choice == "5":
            create_teachers()
        elif choice == "6":
            list_all_teachers()
        elif choice == "7":
            list_teachers_subjects()
        elif choice == "8":
            create_subject()
        elif choice == "9":
            teacher_of_subject()
        elif choice == "10":
            delete_subject()
        elif choice == "11":
            list_all_subjects()
        elif choice == "12":
            update_subject()
        elif choice == "13":
            create_student_subjects()
        elif choice == "14":
            subjects_of_a_student()
        elif choice == "15":
            students_of_a_subject()
        else:
            print("Invalid choice! Select a valid choice.")


if __name__ == "__main__":
    main()


