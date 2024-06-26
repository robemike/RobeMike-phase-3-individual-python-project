from initialization.db_connect import conn, cursor
from .session import Session

class Student:

    all = {}
    
    def __init__(self, first_name, second_name, gender, age, id = None):
        self.id = id 
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.age = age 

    def __repr__(self):
        return f"\t<Student {self.id}: {self.first_name} {self.second_name}, Gender: {self.gender}, Age: {self.age}>"
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and len(value) != 0:
            self._first_name = value
        else:
            raise ValueError(
                "Name must be a non-empty string."
            )
    
    @property
    def second_name(self):
        return self._second_name
    
    @second_name.setter
    def second_name(self, value):
        if isinstance(value, str) and len(value) != 0:
            self._second_name = value
        else:
            raise ValueError(
                "Second name must also be a non-empty string."
            )
    
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if isinstance(value, str) and len(value) == 1:
            self._gender = value
        else:
            raise ValueError(
                "Input gender value 'm' or 'f' (lowercase)"
            )

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self._age  = value 
        else:
            raise ValueError(
                "Age must be a number(integer)."
            )
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS students;
        """
        cursor.execute(sql)
        conn.commit()
        
    def save(self):
        sql = """
            INSERT INTO students (first_name, second_name, gender, age) 
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.first_name, self.second_name, self.gender, self.age))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, first_name, second_name, gender, age):
        student = cls(first_name, second_name, gender, age)
        student.save()
        return student
    
    @classmethod
    def instance_from_db(cls, row):
        student = cls.all.get(row[0])
        if student:
            student.first_name = row[1]
            student.second_name = row[2]
            student.gender = row[3]
            student.age = row[4]
        else:
            student = cls(row[1], row[2], row[3], row[4])
            student.id = row[0]
            cls.all[student.id] = student
        return student    
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM students
        """
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def delete(self):
        sql = """
            DELETE FROM students
            WHERE first_name = ?
        """
        cursor.execute(sql, (self.first_name,))
        conn.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM students WHERE first_name =? OR second_name =?
        """

        row = cursor.execute(sql, (name, name)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM students WHERE id = ? 
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def sessions(self):
        """Return a list of sessions associated with a particular student"""
        sql = """
            SELECT sessions.id, sessions.title, sessions.lecturer_id
            FROM sessions
            INNER JOIN students_sessions
            ON sessions.id = students_sessions.session_id
            INNER JOIN students
            ON students_sessions.student_id = students.id
            WHERE students.id = ? 
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        return [Session.instance_from_db(row) for row in rows]
    
    def school_fees(self):
        from .school_fees import SchoolFees
        """Return a school fee information associated with a particular student"""
        sql = """
            SELECT * FROM school_fees
            INNER JOIN students
            ON school_fees.student_id = students.id
            WHERE students.id =?
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        return [SchoolFees.instance_from_db(row) for row in rows]
    
    def update(self):
        sql = """
            UPDATE students
            SET first_name = ?, second_name = ?, gender = ?, age = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.first_name, self.second_name, self.gender, self.age, self.id))
        conn.commit()