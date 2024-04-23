from src.person import Person
from src.account import Account
from src.loan import Loan

class Customer(Person):
    def __init__(self, name, family, national_code, hometown=None, balance=0, has_taken_loan=False):
        super().__init__(name, family, national_code)
        self.hometown = hometown
        self.loan_number = None
        self.balance = balance
        # self.has_taken_loan = has_taken_loan
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
    
    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance = self.balance + self.deposit_amount
        print(f"Ammount balance has been changed {self.balance}")
        
    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.withdraw_amount > self.balance:
            print(f"Your account balance is insufficient")
            
        else:
            self.balance = self.balance - self.withdraw_amount
            print(f"Ammount balance has been changed {self.balance}")
            
    def request_loan(self, branch_name, loan_amount):
        if branch_name.enable_loan and branch_name.budget > loan_amount:
            if not self.has_taken_loan:
                if self.balance > loan_amount:
                    loan_number = Loan.create_loan_number()
                    new_loan = Loan(loan_number, loan_amount, self.national_code, self.account.account_number, branch.bank_id)
                    branch_name.give_loan(loan_number, loan_amount, self.national_code)
                    self.balance += loan_amount
                    self.has_taken_loan = True
                    print(f"Loan of {loan_amount} granted successfully to Customer {self.name}")
                else:
                    print("Customer does not have enough balance for the loan.")
            else:
                print("Customer has already taken a loan from this branch.")
        else:
            print("Branch cannot grant a loan at the moment.")
            
            
    def show_details(self):
        print(f"Name: {self.name}, Family: {self.family}, National Code: {self.national_code}, Balance: {self.balance}")
        print(f"Accounts: {self.bank_accounts}, Loan Number: {self.loan_number}, Hometown: {self.hometown or 'Not provided'}")