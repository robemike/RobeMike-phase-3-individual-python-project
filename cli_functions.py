from models.student import Student
from models.teacher import Teacher
from models.subject import Subject

def exit_programm():
    print("Exiting the programm ...")
    exit()

def list_all_students():
    students = Student.get_all()
    for student in students:
        print(student)

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
        subject = Subject.create(title, teacher_id)
        print(f"Subject {subject.title} added succesfully")
    except Exception as exc:
        print(f"Error while adding subject: ", exc)

def list_teachers_subjects():
    id_ = input("Enter the teacher's id: ")
    teacher = Teacher.find_by_id(id_)
    if teacher:
        subjects = teacher.subjects()
        for subject in subjects:
            print(subject)
    else:
        print(f"Teacher {id_} does not exist")

def teacher_of_subject():
    id_ = input("Enter the Subject's id: ")
    subject = Subject.find_by_id(id_)
    if subject:
        teacher = subject.teacher()
        if teacher:
            print(f"The teacher for subject {subject.title}.")
        else:
            print("No teacher found for this subject.")
    else:
        print(f"No Subject {id_} found.")