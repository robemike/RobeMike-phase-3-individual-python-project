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
            subject TEXT NOT NULL
        )
    """
    cursor.execute(sql)
    conn.commit
def create_subjects_table():
    sql = """
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT NOT NULL,
            teacher_id INTEGER, 
            FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        )
    """
    cursor.execute(sql)
    conn.commit()

def create_students_subjects_tables():
    sql = """
        CREATE TABLE student_subjects (
            student_id INTEGER,
            subject_id INTEGER, 
            FOREIGN KEY (student_id) REFERENCES students(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    """
    cursor.execute(sql)
    conn.commit()

def create_school_fees_table():
    sql = """
        CREATE TABLE IF NOT EXISTS school_fees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER NOT NULL,
            balance INTEGER NOT NULL,
            student_id INTEGER NOT NULL UNIQUE,
            FOREIGN KEY (student_id) REFERENCES students (id)
        )
    """
    cursor.execute(sql)
    conn.commit()

create_students_table()
create_teachers_table()
create_subjects_table()
create_students_subjects_tables()
create_school_fees_table()

conn.close()