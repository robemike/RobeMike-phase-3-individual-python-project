from initialization.db_connect import conn, cursor
from .student import Student

class SchoolFees:

    all = {}

    def __init__(self, amount, settled, student_id, id = None):
        self.id = id
        self.amount = amount 
        self.settled = settled
        self.student_id = student_id


    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, value):
        if not isinstance(value, int):
            raise ValueError (
                "Amount must be a number(integer)"
            )
        self._amount = value

    @property
    def settled(self):
        return self._settled
    
    @settled.setter
    def settled(self, value):
        if not isinstance(value, int):
            raise ValueError(
                "Balance must be a number(integer)"
            )
        self._settled = value

    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        if type(value) is int and Student.find_by_id(value):
            self._student_id = value
        else:
            ValueError(
                "student_id must reference a student in the database."
            )
    
    def save(self):
        sql = """
            INSERT INTO school_fees (amount, settled, student_id) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.amount, self.settled, self.student_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, amount, settled, student_id):
        student_fees = cls(amount, settled, student_id)
        student_fees.save()
        return student_fees

