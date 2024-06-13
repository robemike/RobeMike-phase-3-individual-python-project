class Student:

    all = {}
    
    def __init__(self, first_name, second_name, gender, age, id = None):
        self.id = id 
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.age = age 

    def __repr__(self):
        return f"<Student :{self.first_name}, {self.second_name}, Gender: {self.gender}, Age: {self.age}>"
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and len(value) > 0:
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
        if isinstance(value, str) and len(value) > 0:
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
        if isinstance(value, str) and value != 0:
            self._gender = value
        else:
            raise ValueError(
                "Gender must be a non_empty string."
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
         
mike = Student("Mike", "Robe", "M", 18)
print(mike)
mike.first_name = 1
print(mike)
    
    # @classmethod
    # def instance_from_db(cls, row):
    #     student = cls.all.get(row[0])
    #     if student:
    #         student.first_name = row[1]
    #         student.second_name = row[2]
    #         student.gender = row[3]
    #         student.age = row[4]
    #     else:
    #         student = cls(row[1], row[2], row[3], row[4])
    #         student.id = row[0]
    #         cls.all[student.id] = student
    #     return student    

    