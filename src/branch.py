from src.bank import Bank
from src.loan import Loan

class Branch(Bank):
    def __init__(self, branch_name, bank_id, city_name, number_of_customer, budget):
        super().__init__(branch_name, bank_id)
        self.number_of_customer = number_of_customer
        self.budget = budget
        self.city_name = city_name
        self.branch_name = branch_name
        self.enable_loan = self.budget 
        self.loans = {}  