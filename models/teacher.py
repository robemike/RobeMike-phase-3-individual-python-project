from initialization.db_connect import conn, cursor
class Teacher:

    all = {}

    def __init__(self, name, subject, id = None):
        self.id = id
        self.name = name
        self.subject = subject

    def __repr__(self):
        return f"<Lecturer :{self._name}, Subject: {self._subject}>"
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) and len(value) == 0:
            raise ValueError(
                "Name must ba a non-empty string."
            )
        self._name = value
    
    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, value):
        if not isinstance(value, str) and len(value) == 0:
            raise ValueError(
                "Subject must be a non-empty string."
            )
        self._subject = value
        
    def save(self):
        sql = """
            INSERT INTO teachers (name, subject) VALUES (?, ?)
        """
        cursor.execute(sql, (self.name, self.subject))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, name, subject):
        teacher = cls(name, subject)
        teacher.save()
        return teacher 
    
    @classmethod
    def instance_from_db(cls, row):
        teacher = cls.all.get(row[0])
        if teacher:
            teacher.name = row[1]
            teacher.subject = row[2]
        else:
            teacher = cls(row[1], row[2])
            teacher.id = row[0]
            cls.all[teacher.id] = teacher   
        return teacher
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM teachers WHERE id = ?
        """
        row = cursor.execute(sql, (id)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM teachers WHERE name = ?
        """
        row = cursor.execute(sql, (name)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM teachers 
        """
        rows = cursor.execute(sql)
        rows.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def delete(self):
        sql = """
            DELETE FROM teachers 
            WHERE id =?
        """
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    
    

    # @classmethod
    # def get_all(cls)

    
    

    # Return the lecturer object with values corresponding to a Table row with the ame values based off of the primary key within the table. 
lecturer = Teacher("Mike", "Software Engineering")
print(lecturer)
# lecturer.name = 1
# print(lecturer)