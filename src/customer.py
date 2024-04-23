from src.person import Person
from src.account import Account


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
               
    def deposit_and_get_account_number(self, initial_amount):
        account_number = self.create_account(initial_amount)
        
        return account_number

    def create_account(self, initial_amount):
        account = Account(initial_amount)
        account.creat_account_number()
        
        return account.creat_account_number