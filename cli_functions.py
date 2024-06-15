from models.student import Student
from models.teacher import Teacher
from models.subject import Subject
from models.student_subjects import StudentsSubjects
# from models.school_fees import SchoolFees

def exit_programm():
    print("Exiting the programm ...")
    exit()

# STUDENT'S MODEL

# To refer to this.
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



# THE TEACHERS MODEL:
def create_teachers():
    name = input("Enter the Teacher's name: ")
    subject = input("Enter the subject that the teacher teaches: ")
    try:
        teacher = Teacher.create(name, subject)
        print(f"Teacher {teacher.name} added.")
    except Exception as exc:
        print(f"Error while adding teacher: ", exc)

def list_all_teachers():
    teachers = Teacher.get_all()
    for teacher in teachers:
        print(teacher)

def list_teachers_subjects():
    id_ = input("Enter the teacher's id: ")
    teacher = Teacher.find_by_id(id_)
    if teacher:
        subjects = teacher.subjects()
        for subject in subjects:
            print(subject)
    else:
        print(f"Teacher {id_} does not exist")

def delete_teacher():
    name = input("Enter the teacher's name: ")
    if teacher := Teacher.find_by_name(name):
        teacher.delete()
        print(f"Teacher {teacher.name} deleted.")
    else:
        print(f"Teacher {teacher.name} not found.")


# SUBJECT MODEL
def create_subject():
    title = input("Enter the subject title: ")
    teacher_id = input("ID of the teacher associated with the subject: ")
    try:
        subject = Subject.create(title, int(teacher_id))
        print(f"{subject} added succesfully")
    except Exception as exc:
        print(f"Error while adding subject: ", exc)

def list_all_subjects():
    subjects = Subject.get_all()
    for subject in subjects:
        print(subject)

def teacher_of_subject():
    id_ = input("Enter the Subject's id: ")
    subject = Subject.find_by_id(id_)
    if subject:
        teacher = subject.teacher()
        if teacher:
            print(f"Subject {subject.title} handled by teacher {teacher.name}.")
        else:
            print("No teacher found for this subject.")
    else:
        print(f"No Subject {id_} found.")

def delete_subject():
    id_ = input("Enter the ID of the subject you wish to delete: ")
    if subject := Subject.find_by_id(id_):
        subject.delete()
        print(f"Subject {subject.title} deleted.")
    else:
        print(f"Subject {id_} not found. ")

def update_subject():
    id_ = input("Enter the id of the subject you wish to update: ")
    if subject := Subject.find_by_id(id_):
        try:
            teacher_id = input("Enter the id of the new teacher handing the subject.")
            subject.teacher_id = teacher_id
            subject.update()
            print(f"Success: {subject}")
        except Exception as exc:
            print("Error updating subject: ", exc)
    else:
        print(f"Subject {id_} not found in database.")

# STUDENT_SUBJECTS RELATIONSHIP(JOIN TABLE)

def create_student_subjects():
    student_id = input("Enter the student's id: ")
    subject_id = input("Enter the subject's id: ")
    try:
        student_subject = StudentsSubjects.create(int(student_id), int(subject_id))
        print(f"Success {student_subject.student_id} ID and {student_subject.subject_id} ID added")
    except Exception as exc:
        print("Error adding: ", exc)

def subjects_of_a_student():
    id_ = input("Enter the Student's id whose subjects you want to see: ")
    student = Student.find_by_id(id_)
    if student:
        subjects = student.subjects()
        for subject in subjects:
            print(subject)
    else:
        print(f"Student {id_} does not exist.")

def students_of_a_subject():
    id_ = input("Enter the subject's id whose students you want to see.")
    id_ = id_
    subject = Subject.find_by_id(id_)
    if subject:
        students = subject.students()
        for student in students:
            print(student)
    else:
        print(f"Subject {id_} does not exists.")

def create_student_fees():
    pass