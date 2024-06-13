from models.student import Student
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
