from initialization.db_connect import conn, cursor
from .student import Student

class SchoolFees:
    def __init__(self, amount, balance, student_id, id = None):
        self.id = id
        self.amount = amount 
        self.balance = balance
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
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if not isinstance(value, int):
            raise ValueError(
                "Balance must be a number(integer)"
            )
        self._balance = value

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
    
    def __repr__(self):
        return f"The school fee amount is"
    
    def make_payment(self, amount_paid):
        if amount_paid == 0:
            print("Kindly pay your child's fee.")
        elif amount_paid > self.balance:
            print("Payment amount exceeds the current balance.")
        else:
            self.balance -= amount_paid
            print(f"Payment successful. Remaining balance: {self.balance}")

    def add_fees(self, additional_amount):
        if additional_amount <= 0:
            print("Invalid additional fee amount. Please enter a positive value.")
        else :
            self.amount += additional_amount
            print(f"Additional fee amount added. New total fee amount: {self.amount}")
    
    def save(self):
        sql = """
            INSERT INTO school_fees (amount, balance, student_id) VALUES (?, ?, ?)
        """
        cursor.execute(sql, (self.amount, self.balance, self.student_id))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, amount, balance):
        student_fees = cls(amount, balance)
        student_fees.save()
        return student_fees

