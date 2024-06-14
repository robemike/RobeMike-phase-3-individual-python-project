from initialization.db_connect import conn, cursor
class Student:

    all = {}
    
    def __init__(self, first_name, second_name, gender, age, id = None):
        self.id = id 
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.age = age 
        # self.class = class

    def __repr__(self):
        return f"<Student :{self.first_name}, {self.second_name}, Gender: {self.gender}, Age: {self.age}>"
        
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
    # Save the object in the dictionary using the Table row P.K as dict key
    def save(self):
        # Create an SQL statement to insert a new row to the table with the values corresponding to the object attribute values. 
        sql = """
            INSERT INTO students (first_name, second_name, gender, age) 
            VALUES (?, ?, ?, ?)
        """
        cursor.execute(sql, (self.first_name, self.second_name, self.gender, self.age))
        conn.commit()
        # Object id attribute(which was set to None) is updated using the P.K value of the new row saved to the database.
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, first_name, second_name, gender, age):
        # Initialize a new student instance.
        student = cls(first_name, second_name, gender, age)
        # Save the object to the database.
        student.save()
        return student

    # Returns the student object having the same values as the those on the table row.
    @classmethod
    def instance_from_db(cls, row):
        # Check the dictionary all for an existing instance using the row's primary key.
        student = cls.all.get(row[0])
        # Ensure that the Attributes match the row values.
        if student:
            student.first_name = row[1]
            student.second_name = row[2]
            student.gender = row[3]
            student.age = row[4]
            # If not in the all dictionary, create a new instance and add to the all dictionary.
        else:
            student = cls(row[1], row[2], row[3], row[4])
            student.id = row[0]
            cls.all[student.id] = student
        return student    
    
    @classmethod
    def get_all(cls):
        # Return a list containing the student objects per row in the table.
        sql = """
            SELECT * FROM students
        """
        rows = cursor.execute(sql)
        rows.fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def delete(self):
        # Delete the table row corresponding to the current student instance/ delete the dict entry/reassign id attribute.
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
        # Return the student object in correspondance to the table row matching the specified P.K
        sql = """
            SELECT * FROM students WHERE first_name =? OR second_name =?
        """

        row = cursor.execute(sql, (name, name)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    # def update(self):
    #     sql = """
    #         UPDATE students
    #         SET age = ?
    #         WHERE naem
    #     """


# mike = Student(1, "Robe", "M", 18)
# print(mike)