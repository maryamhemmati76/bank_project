from src.person import Person

class Customer(Person):
    def __init__(self, name, family, national_code, hometown=None, balance=0, has_taken_loan=False):
        super().__init__(name, family, national_code)
        self.hometown = hometown
        self.loan_number = None
        self.balance = balance
        self.has_taken_loan = has_taken_loan
        self.bank_accounts = []
        self.account = None
        self.has_taken_loan = False
    
    def get_hometown(self):
        print(f"The hometown of {self.name} is {self.hometown}.")
               