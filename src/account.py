import random  
class Account:
    def __init__(self,initial_amount):
        self.initial_amount = initial_amount
        
    def creat_account_number(self):
        random_numbers = []
        
        for i in range(0, 10):
            random_numbers.append(str(random.randint(0, 9)))
            account_number = ''.join(random_numbers)
        
        print(f"Your account number is: {account_number}")  
        return account_number
    