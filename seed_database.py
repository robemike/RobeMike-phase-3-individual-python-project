from models.student import Student
from models.lecturer import Lecturer

def seed_database():
    Student.create("Mohammed", "Bidu", "m", 18)
    Student.create("Mike", "Tyson", "m", 15)
    Student.create("Emma", "Watson", "f", 17)
    Student.create("John", "Doe", "m", 16)
    Student.create("Alice", "Smith", "f", 18)
    Student.create("Bob", "Jones", "m", 17)
    Student.create("Ella", "Johnson", "f", 16)
    Student.create("David", "Brown", "m", 15)
    Student.create("Sophia", "Garcia", "f", 17)
    Student.create("James", "Martinez", "m", 18)
    Student.create("Olivia", "Lopez", "f", 16)
    Student.create("William", "Gonzalez", "m", 15)
    Student.create("Isabella", "Miller", "f", 18)
    Student.create("Michael", "Davis", "m", 17)
    Student.create("Ava", "Rodriguez", "f", 16)

    Lecturer.create("")