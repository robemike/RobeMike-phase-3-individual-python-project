from initialization.db_connect import conn, cursor
from .teacher import Teacher

class Subject:

    all = {}

    def __init__(self, title, teacher_id, id = None):
        self.id = id
        self.title = title
        self.teacher_id = teacher_id

    def __repr__(self):
        return (f"<Subject {self.id}: {self.title}, " + 
               f"Teacher ID: {self.teacher_id}>"
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
    def teacher_id(self):
        return self._teacher_id

    @teacher_id.setter
    def teacher_id(self, value):
        if type(value) is int and Teacher.find_by_id(value):
            self._teacher_id = value
        else:
            raise ValueError(
                "teacher_id must reference a teacher in the database."
            )

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
    
    # def teacher(self):
    #     from .teacher import Teacher 
    #     sql = """
    #         SELECT teachers.name 
    #         FROM teachers 
    #         INNER JOIN subjects 
    #         ON teachers.id = subjects.teacher_id 
    #         WHERE subjects.id = ?
    #     """
    #     cursor.execute(sql, (self.id,),)
    #     row = cursor.fetchone()
    #     if row:
    #         return Teacher.instance_from_db(row)
    #     else:
    #         return None
    
    # def teacher(self):
    #     from .teacher import Teacher 
    #     sql = """
    #         SELECT * FROM teachers 
    #         WHERE id = ? 
    #     """
    #     cursor.execute(sql, (self.teacher_id,),)
    #     row = cursor.fetchone()
    #     return Teacher.instance_from_db(row) if row else None
