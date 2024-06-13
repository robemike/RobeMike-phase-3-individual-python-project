from __init__ import conn, cursor

def create_students_table():
    sql = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL, 
            second_name TEXT NOT NULL, 
            gender TEXT NOT NULL, 
            age INTGER
        )
    """
    cursor.execute(sql)
    conn.commit()
def create_lecturers_table():
    sql = """
        CREATE TABLE IF NOT EXISTS lecturers (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL,
            session TEXT NOT NULL
        )
    """
    cursor.execute(sql)
    conn.commit
def create_sessions_table():
    sql = """
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,
            lecturer_id INTEGER, 
            FOREIGN KEY (lecturer_id) REFERENCES lecturers(id)
        )
    """
    cursor.execute(sql)
    conn.commit()

def create_students_sessions_tables():
    sql = """
        CREATE TABLE student_sessions (
            student_id INTEGER,
            session_id INTEGER, 
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (session_id) REFERENCES sessions(id)
        )
    """
    cursor.execute(sql)
    conn.commit()

create_students_table()
create_lecturers_table()
create_sessions_table()
create_students_sessions_tables()

conn.close()