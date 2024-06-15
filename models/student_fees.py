class StudentFees:
    def __init__(self, amount, balance):
        self.amount = amount 
        self.balance = balance
    
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
        