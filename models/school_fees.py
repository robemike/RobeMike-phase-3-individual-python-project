from initialization.db_connect import conn, cursor
from .student import Student

class SchoolFees:

    all = {}

    def __init__(self, amount, settled, student_id, id = None):
        self.id = id
        self.amount = amount 
        self.settled = settled
        self.student_id = student_id

    def __repr__(self):
        return f"<School Fees {self.id}: Amount: {self.amount}, Settled: {self.settled}, Balance: {self.amount - self.settled}, Student ID: {self.student_id}>"

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
    
    @classmethod
    def instance_from_db(cls, row):
        school_fees = cls.all.get(row[0])
        if school_fees:
            school_fees.amount = row[1]
            school_fees.settled = row[2]
            school_fees.balance = row[3]
            school_fees.student_id = row[4]
        else:
            school_fees = cls(row[1], row[2], row[3], row[4])
            school_fees.id = row[0]
            cls.all[school_fees.id] = school_fees
        return school_fees

