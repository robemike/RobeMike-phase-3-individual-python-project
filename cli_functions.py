from models.student import Student
from models.lecturer import Lecturer
from models.session import Session
from models.students_sessions import StudentsSessions
from models.school_fees import SchoolFees

def exit_programm():
    print("Exiting the programm ...")
    exit()

# STUDENT'S MODEL
def feed_database():
    student_first_name = input("Enter the student's first name: ")

    student_second_name = input("Enter the student's second name: ")

    student_gender = input("Gender strictly (m /f): ")

    student_age = int(input("Student's age: "))

    lecturer_first_name = input("Enter the lecturer's first_name who is teaching the student: ")

    lecturer_second_name = input("Enter the lecturer's second_name who is teaching the student: ")

    session_title = input("Enter the session title: ")

    lecturer_id = int(input("Enter id of the lecturer associated with the session: "))

    student_id = int(input("Enter the student's id associated with the session: "))

    session_id = int(input("Enter the session's id associated with the student: "))
    try:
        student = Student.create(student_first_name, student_second_name, student_gender, student_age)
        print(f"\t\t>Student {student.first_name} {student.second_name} added successfully to the programm.")

        lecturer = Lecturer.create(lecturer_first_name, lecturer_second_name)
        print(f"\t\t>lecturer {lecturer.first_name} {lecturer.second_name} added successfully to the programm.")

        session = Session.create(session_title, int(lecturer_id))
        print(f"\t\t>Session {session.title} added succesfully to the programm.")

        students_session = StudentsSessions.create(int(student_id), int(session_id))
        print(f"\t\t>Success, {students_session.student_id} ID and {students_session.session_id} ID added")

    except Exception as exc:
        print("Error feeding the database: ", exc)

def list_all_students():
    students = Student.get_all()
    for student in students:
        print(student)

def delete_student():
    id_ = input("Enter the student's id: ")
    if student := Student.find_by_id(id_):
        student.delete()
        print(f"\t\t>Student {student.first_name} {student.second_name} deleted successfully.")
    else:
        print(f"\t\t>Student {id_} not found.")

def find_student_by_id():
    id_ = input("Enter the Student's id: ")
    student = Student.find_by_id(id_)
    print(student) if student else print(
        f"\t\t>Student {id_} not found."
    )

def update_student():
    id_ = int(input("Enter the Student's id you wish to update: "))
    if student := Student.find_by_id(id_):
        try:
            first_name = input("Enter the student's first name: ")
            student.first_name = first_name
            second_name = input("Enter the student's second name: ")
            student.second_name = second_name
            gender = input("Enter the student's gender [Strictly (m/f)]: ")
            student.gender = gender
            age = int(input("Enter the student's age: "))
            student.age = age
            student.update()
            print(f"\t\t>Success: {student}")
        except Exception as exc:
            print("Error updating student: ", exc)
    else:
        print(f"Student {id_} not found in database.")

def list_all_lecturers():
    lecturers = Lecturer.get_all()
    for lecturer in lecturers:
        print(lecturer)

def list_lecturers_sessions():
    id_ = input("Enter the lecturer's id: ")
    lecturer = Lecturer.find_by_id(id_)
    if lecturer:
        sessions = lecturer.sessions()
        for session in sessions:
            print(session)
    else:
        print(f"\t\t>lecturer {id_} does not exist")

def update_lecturer():
    id_ = int(input("Enter the id of the lecturer you wish to update: "))
    if lecturer := Lecturer.find_by_id(id_):
        try:
            first_name = input("Enter the lecturer's first name: ")
            lecturer.first_name = first_name
            second_name = input("Enter the lecturer's second name: ")
            lecturer.second_name = second_name
            lecturer.update()
            print(f"\t\t>Success: {lecturer}")
        except Exception as exc:
            print("Error updating lecturer: ", exc)
    else:
        print(f"Lecturer {id_} not found in database.") 

def delete_lecturer():
    id_ = input("Enter the lecturer's id you want to remove: ")
    if lecturer := Lecturer.find_by_id(id_):
        lecturer.delete()
        print(f"\t\t>lecturer {lecturer.first_name} {lecturer.second_name} deleted successfully.")
    else:
        print(f"\t\t>lecturer {id_} not found.")


# SESSION MODEL

def list_all_sessions():
    sessions = Session.get_all()
    for session in sessions:
        print(session)

def lecturer_of_session():
    id_ = input("Enter the session's id: ")
    session = Session.find_by_id(id_)
    if session:
        lecturer = session.lecturer()
        if lecturer:
            print(f"\t\t>Session {session.title} handled by lecturer {lecturer.first_name} {lecturer.second_name}.")
        else:
            print("\t\t>No lecturer found for this session.")
    else:
        print(f"\t\t>No session {id_} found.")

def delete_session():
    id_ = input("Enter the ID of the session you wish to delete: ")
    if session := Session.find_by_id(id_):
        session.delete()
        print(f"\t>Success: \n\t\tSession {session.title} deleted.")
    else:
        print(f"\t\tSession {id_} not found. ")

def update_session():
    id_ = int(input("Enter the id of the session you wish to update: "))
    if session := Session.find_by_id(id_):
        try:
            title = input("Enter the session's title: ")
            session.title = title
            lecturer_id = int(input("Enter the id of the new lecturer handing the session: "))
            session.lecturer_id = lecturer_id
            session.update()
            print(f"\t\t>Success: {session}")
        except Exception as exc:
            print("\t\t>Error updating session: ", exc)
    else:
        print(f"\t\t>Session {id_} not found in database.")

# STUDENT_SESSIONS RELATIONSHIP(JOIN TABLE)


def sessions_of_a_student():
    id_ = input("Enter the Student's id whose sessions you want to see: ")
    student = Student.find_by_id(id_)
    if student:
        sessions = student.sessions()
        for session in sessions:
            print(session)
    else:
        print(f"\t\t>Student {id_} does not exist.")

def students_of_a_session():
    id_ = input("Enter the session's id whose students you want to see: ")
    session = Session.find_by_id(id_)
    if session:
        students = session.students()
        for student in students:
            print(student)
    else:
        print(f"\t\t>session {id_} does not exists.")

def create_student_fees():
    amount = int(input("Enter the school fee amount: "))
    settled = int(input("Enter the settled amount: "))
    student_id = int(input("Enter the student id: "))
    try:
        schoool_fees = SchoolFees.create(amount, settled, student_id)
        print(f"\t\t>School fees of student:{schoool_fees.student_id} added successfully.")
    except Exception as exc:
        print("\t\t>Error adding: ", exc)

def student_school_fee():
    id_ = int(input("Enter the student's id: "))
    student = Student.find_by_id(id_)
    if student:
        school_fees = student.school_fees()
        for school_fee in school_fees:
            print(f"School fee of information of {student.first_name} {student.second_name} is: {school_fee}")
    else:
        print(f"\t\t>Student {id_} does not exist.")

def update_students_fee():
    student_id = int(input("Enter the student's id whose fee you want to update: "))
    if school_fee := SchoolFees.find_by_student_id(student_id):
        try:
            amount = int(input("Enter the amount of fees: "))
            school_fee.amount = amount
            settled = int(input("Enter the new settled amount: "))
            school_fee.settled = settled
            
            school_fee.update()
            print(f"\t>Success fee of student id {student_id}: {school_fee} updated")
        except Exception as exc:
            print("\t\t>Error updating school fee: ", exc)
    else:
        print(f"\t\t>Student {student_id} not found.")