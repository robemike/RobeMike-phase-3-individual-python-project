from models.student import Student
from models.lecturer import Lecturer
from models.session import Session
from models.students_sessions import StudentsSessions
from models.school_fees import SchoolFees
from initialization.create_tables import create_lecturers_table, create_sessions_table, create_school_fees_table, create_students_sessions_tables, create_students_table
from initialization.db_connect import conn

def seed_database():
    Student.drop_table()
    Session.drop_table()
    StudentsSessions.drop_table()
    Lecturer.drop_table()
    SchoolFees.drop_table()
    create_students_table()
    create_lecturers_table()
    create_school_fees_table()
    create_sessions_table()
    create_students_sessions_tables()
    students_data = [
    ("Mohammed", "Bidu", "m", 18),
    ("Mike", "Tyson", "m", 15),
    ("Emma", "Watson", "f", 17),
    ("John", "Doe", "m", 16),
    ("Alice", "Smith", "f", 18),
    ("Bob", "Jones", "m", 17),
    ("Ella", "Johnson", "f", 16),
    ("David", "Brown", "m", 15),
    ("Sophia", "Garcia", "f", 17),
    ("James", "Martinez", "m", 18)
    ]

    for data in students_data:
        Student.create(*data)

    lecturers_data = [
    ("Mike", "Smith"),
    ("John", "Doe"),
    ("Emily", "Johnson"),
    ("Sarah", "Brown"),
    ("David", "Wilson")
    ]

    for data in lecturers_data:
        Lecturer.create(*data)

    sessions_data = [
    ("Software Engineering", 3),
    ("Database Management", 4),
    ("Data Structures", 2),
    ("Network Security", 3),
    ("Artificial Intelligence", 4),
    ("Machine Learning", 5),
    ("Web Development", 1),
    ("Mobile App Development", 2),
    ("Cloud Computing", 1),
    ("Cybersecurity", 5)
    ]

    for data in sessions_data:
        Session.create(*data)

    students_sessions_data = [
    [2, 1], [4, 1], [2, 2], [4, 2],
    [1, 3], [3, 3], [1, 4], [3, 4],
    [5, 5], [6, 5], [5, 6], [6, 6],
    [7, 7], [8, 7], [7, 8], [8, 8],
    [9, 9], [10, 9], [9, 10], [10, 10]
    ]

    for data in students_sessions_data:
        StudentsSessions.create(data[0], data[1])

    school_fees_data = [
    [50000, 20000, 1],
    [50000, 37000, 2],
    [50000, 50000, 3],
    [50000, 40000, 4],
    [50000, 45000, 5],
    [50000, 25000, 6],
    [50000, 34000, 7],
    [50000, 30000, 8],
    [50000, 13000, 9],
    [50000, 29000, 10]
    ]

    for data in school_fees_data:
        SchoolFees.create(data[0], data[1], data[2])

seed_database()
print("Seeded database.")

conn.close()