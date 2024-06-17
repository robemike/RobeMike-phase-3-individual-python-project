from initialization.db_connect import conn, cursor
from .student import Student

class SchoolFees:

    all = {}

    def __init__(self, amount, settled, student_id, id = None):
        self.id = id
        self.amount = amount 
        self.settled = settled
        self._student_id = student_id

    def __repr__(self):
        return f"\n\t\t< Amount: {self.amount}, \n\t\tSettled: {self.settled}, \n\t\tBalance: {self.amount - self.settled}>"

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
                "Settled amt must be a number(integer)"
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
            raise ValueError("student_id must reference a student in the database.")
    
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
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS school_fees;
        """
        cursor.execute(sql)
        conn.commit()
    
    def update(self):
        """Update a student's fee."""
        sql = """
            UPDATE school_fees
            SET amount = ?, settled = ?
            WHERE student_id = ? 
        """
        cursor.execute(sql, (self.amount, self.settled, self.student_id))
        conn.commit()

    @classmethod
    def find_by_student_id(cls, student_id):
        sql = """
            SELECT * FROM school_fees WHERE student_id = ? 
        """
        row = cursor.execute(sql, (student_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
