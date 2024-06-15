from initialization.db_connect import conn, cursor
from .student import Student
from .session import Session

class StudentsSessions:

    all = {}

    def __init__(self, student_id, session_id):
        self.student_id = student_id
        self.session_id = session_id

    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        if type(value) is int and Student.find_by_id(value):
            self._student_id = value
        else:
            raise ValueError(
                "Student id must reference a student in the database."
            )
        
    @property
    def session_id(self):
        return self._session_id
    
    @session_id.setter
    def session_id(self, value):
        if type(value) is int and Session.find_by_id(value):
            self._session_id = value
        else:
            raise ValueError(
                "session id must reference a session in the database."
            )
        
    def save(self):
        sql = """
            INSERT INTO students_sessions (student_id, session_id) 
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.student_id, self.session_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, student_id, session_id):
        student_session = cls(student_id, session_id)
        student_session.save()
        return student_session