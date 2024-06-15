from initialization.db_connect import conn, cursor
from .student import Student
from .subject import Subject

class StudentsSubjects:

    all = {}

    def __init__(self, student_id, subject_id):
        self.student_id = student_id
        self.subject_id = subject_id

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
    def subject_id(self):
        return self._subject_id
    
    @subject_id.setter
    def subject_id(self, value):
        if type(value) is int and Subject.find_by_id(value):
            self._subject_id = value
        else:
            raise ValueError(
                "subject id must reference a subject in the database."
            )
        
    def save(self):
        sql = """
            INSERT INTO student_subjects (student_id, subject_id) 
            VALUES (?, ?)
        """
        cursor.execute(sql, (self.student_id, self.subject_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, student_id, subject_id):
        student_subject = cls(student_id, subject_id)
        student_subject.save()
        return student_subject