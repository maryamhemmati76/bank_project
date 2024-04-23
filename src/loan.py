import uuid       
     
class Loan:
    def __init__(self, loan_amount, national_code, account_number, branch_name):
        self.loan_amount = loan_amount
        self.national_code = national_code
        self.account_number = account_number
        self.branch_name = branch_name
    
    def create_loan_number(self):
        loan_number =  str(uuid.uuid4())
        print(f"Unique Loan Number: {loan_number}")
        
    def show_details(self):
        print(f"Loan Number: {self.loan_number}, Amount: {self.loan_amount}")
        print(f"Customer ID: {self.national_code}, Account ID: {self.account_id}, Branch ID: {self.branch_id}")