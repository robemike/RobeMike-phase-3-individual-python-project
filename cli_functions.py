from models.student import Student
from models.lecturer import Lecturer
from models.session import Session
from models.students_sessions import StudentsSessions
from models.school_fees import SchoolFees

def exit_programm():
    print("Exiting the programm ...")
    exit()

# STUDENT'S MODEL
def create_students():
    first_name = input("Enter the Student's first name: ")
    second_name = input("Enter the student's second name: ")
    gender = input("Gender: ")
    age = input("Student's age: ")
    age = int(age)
    try:
        student = Student.create(first_name, second_name, gender, age)
        print(f"Student {student.first_name} {student.second_name} added.")
    except Exception as exc:
        print("Error adding: ", exc)

def list_all_students():
    students = Student.get_all()
    for student in students:
        print(student)

# To refer to this (lowercase)
def delete_student():
    name = input("Enter the student's name: ")
    if student := Student.find_by_name(name):
        student.delete()
        print(f"Student {student.first_name} {student.second_name} deleted.")
    else:
        print(f"Student {name} not found.")

def find_student_by_id():
    id_ = input("Enter the Student's id: ")
    student = Student.find_by_id(id_)
    print(student) if student else print(
        f"Student {id_} not found."
    )

# THE LECTURER MODEL:
def create_lecturers():
    name = input("Enter the lecturer's name: ")
    session = input("Enter the session that the lecturer teaches: ")
    try:
        lecturer = Lecturer.create(name, session)
        print(f"lecturer {lecturer.name} added.")
    except Exception as exc:
        print(f"Error while adding lecturer: ", exc)

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
        print(f"lecturer {id_} does not exist")

def delete_lecturer():
    name = input("Enter the lecturer's name: ")
    if lecturer := Lecturer.find_by_name(name):
        lecturer.delete()
        print(f"lecturer {lecturer.name} deleted.")
    else:
        print(f"lecturer {lecturer.name} not found.")


# session MODEL
def create_session():
    title = input("Enter the session title: ")
    lecturer_id = input("ID of the lecturer associated with the session: ")
    try:
        session = Session.create(title, int(lecturer_id))
        print(f"{session} added succesfully")
    except Exception as exc:
        print(f"Error while adding session: ", exc)

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
            print(f"session {session.title} handled by lecturer {lecturer.name}.")
        else:
            print("No lecturer found for this session.")
    else:
        print(f"No session {id_} found.")

def delete_session():
    id_ = input("Enter the ID of the session you wish to delete: ")
    if session := Session.find_by_id(id_):
        session.delete()
        print(f"session {session.title} deleted.")
    else:
        print(f"session {id_} not found. ")

def update_session():
    id_ = input("Enter the id of the session you wish to update: ")
    if session := Session.find_by_id(id_):
        try:
            lecturer_id = input("Enter the id of the new lecturer handing the session.")
            session.lecturer_id = lecturer_id
            session.update()
            print(f"Success: {session}")
        except Exception as exc:
            print("Error updating session: ", exc)
    else:
        print(f"session {id_} not found in database.")

# STUDENT_sessionS RELATIONSHIP(JOIN TABLE)

def create_students_sessions():
    student_id = input("Enter the student's id: ")
    session_id = input("Enter the session's id: ")
    try:
        students_session = StudentsSessions.create(int(student_id), int(session_id))
        print(f"Success {students_session.student_id} ID and {students_session.session_id} ID added")
    except Exception as exc:
        print("Error adding: ", exc)

def sessions_of_a_student():
    id_ = input("Enter the Student's id whose sessions you want to see: ")
    student = Student.find_by_id(id_)
    if student:
        sessions = student.sessions()
        for session in sessions:
            print(session)
    else:
        print(f"Student {id_} does not exist.")

def students_of_a_session():
    id_ = input("Enter the session's id whose students you want to see.")
    session = Session.find_by_id(id_)
    if session:
        students = session.students()
        for student in students:
            print(student)
    else:
        print(f"session {id_} does not exists.")

# def create_student_fees():
#     try:
#         default_amount = int(input("Enter the default amount of school fees: "))
#         settled = int(input("Enter the initial balance: "))
#         student_id = int(input("Enter the student ID: "))
        
#         school_fees = SchoolFees.create(settled, student_id, default_amount=default_amount)
        
#         print(f"School fees for student {school_fees.student_id} added successfully.")
#     except Exception as exc:
#         print("Error adding fees: ", exc)

def create_student_fees():
    amount = int(input("Enter the school fee amount: "))
    settled = int(input("Enter the settled amount: "))
    student_id = int(input("Enter the student id: "))
    try:
        schoool_fees = SchoolFees.create(amount, settled, student_id)
        print(f"School fees of student:{schoool_fees.student_id} added successfully.")
    except Exception as exc:
        print("Error adding: ", exc)

def student_school_fee():
    id_ = int(input("Enter the student's id: "))
    student = Student.find_by_id(id_)
    if student:
        school_fees = student.school_fees()
        for school_fee in school_fees:
            print(school_fee)
    else:
        print(f"Student {id_} does not exist.")