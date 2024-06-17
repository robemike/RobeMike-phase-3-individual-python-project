from initialization.db_connect import conn, cursor
from .lecturer import Lecturer

class Session:

    all = {}

    def __init__(self, title, lecturer_id, id = None):
        self.id = id
        self.title = title
        self.lecturer_id = lecturer_id

    def __repr__(self):
        return (f"\t<Session {self.id}: {self.title}, " + 
               f"lecturer ID: {self.lecturer_id}>"
        )
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str) and len(value) == 0:
            raise ValueError(
                "Title must be a non-empty string"
            )
        self._title = value

    @property
    def lecturer_id(self):
        return self._lecturer_id

    @lecturer_id.setter
    def lecturer_id(self, value):
        if type(value) is int and Lecturer.find_by_id(value):
            self._lecturer_id = value
        else:
            raise ValueError(
                "lecturer_id must reference a lecturer in the database and be an integer."
            )
        
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS sessions;
        """
        cursor.execute(sql)
        conn.commit()

    def save(self):
        sql = """
            INSERT INTO sessions (title, lecturer_id) VALUES (?, ?)
        """
        cursor.execute(sql, (self.title, self.lecturer_id))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, lecturer_id):
        subject = cls(title, lecturer_id)
        subject.save()
        return subject
    
    @classmethod
    def instance_from_db(cls, row):
        subject = cls.all.get(row[0])
        if subject:
            subject.title = row[1]
            subject.lecturer_id = row[2]
        else:
            subject = cls(row[1], row[2])
            subject.id = row[0]
            cls.all[subject.id] = subject
        return subject
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM sessions
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def delete(self):
        sql = """
            DELETE FROM sessions 
            WHERE id =?
        """
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM sessions WHERE id = ? 
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def update(self):
        sql = """
            UPDATE sessions SET title = ?, lecturer_id = ? 
            WHERE id = ? 
        """
        cursor.execute(sql, (self.title, self.lecturer_id, self.id))
        conn.commit()

    def students(self):
        from .student import Student
        sql = """
            SELECT students.id, students.first_name, students.second_name,
            students.gender, students.age
            FROM students
            INNER JOIN students_sessions
            ON students.id = students_sessions.student_id
            INNER JOIN sessions
            ON students_sessions.session_id = sessions.id
            WHERE sessions.id = ? 
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        return [Student.instance_from_db(row) for row in rows]

    def lecturer(self):
        from .lecturer import Lecturer 
        sql = """
            SELECT * FROM lecturers 
            INNER JOIN sessions 
            ON lecturers.id = sessions.lecturer_id 
            WHERE sessions.id = ?
        """
        cursor.execute(sql, (self.id,),)
        row = cursor.fetchone()
        if row:
            return Lecturer.instance_from_db(row)
        else:
            return None