from models.student import Student
def exit_programm():
    print("Exiting the programm ...")
    exit()

def list_all_students():
    students = Student.get_all()
    for student in students:
        print(student)

def create_students():
    first_name = input("Enter the Student's first name: ")
    second_name = input("Enter the student's second name: ")
    gender = input("Gender: ")
    age = input("Student's age: ")
    try:
        student = Student.create(first_name, second_name, gender, age==int)
        print(f"Student {student.first_name} {student.second_name} added.")
    except Exception as exc:
        print("Error adding: ", exc)