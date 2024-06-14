from initialization.db_connect import conn, cursor

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
