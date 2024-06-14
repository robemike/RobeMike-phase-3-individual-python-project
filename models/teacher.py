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
        return self.subject
    
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
        
    classmethod
    def create(cls, name, subject):
        teacher = cls(name, subject)
        teacher.save()
        return teacher 
    

    # @classmethod
    # def get_all(cls)

    
    

    # Return the lecturer object with values corresponding to a Table row with the ame values based off of the primary key within the table. 
lecturer = Teacher("Mike", "Software Engineering")
print(lecturer)
# lecturer.name = 1
# print(lecturer)