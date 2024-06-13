from db_connect import conn, cursor

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
def create_teachers_table():
    sql = """
        CREATE TABLE IF NOT EXISTS teachers (
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
            teacher_id INTEGER, 
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
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
create_teachers_table()
create_sessions_table()
create_students_sessions_tables()

conn.close()