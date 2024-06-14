from initialization.db_connect import conn, cursor
from .teacher import Teacher

class Subject:

    all = {}

    def __init__(self, title, teacher_id, id = None):
        self.id = id
        self.title = title
        self.teacher_id = teacher_id

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
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        if type(value) is str and Teacher.find:
            pass

    def save(self):
        sql = """
            INSERT INTO subjects (title, teacher_id) VALUES (?, ?)
        """
        cursor.execute(sql, (self.title, self.teacher_id))
        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, teacher_id):
        subject = cls(title, teacher_id)
        subject.save()
        return subject
    
    @classmethod
    def instance_from_db(cls, row):
        subject = cls.all.get(row[0])
        if subject:
            subject.title = row[1]
            subject.teacher_id = row[2]
        else:
            subject = cls(row[1], row[2])
            subject.id = row[0]
            cls.all[subject.id] = subject
            return subject
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM subjects
        """
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def delete(self):
        sql = """
            DELETE FROM subjects 
            WHERE id =?
        """
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM subjects WHERE id = ? 
        """
        row = cursor.execute(sql, (id)).fetchone()
        return cls.instance_from_db(row) if row else None
