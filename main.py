from src.customer import Customer
from src.branch import Branch

name = input("Enter your name: ")
family = input("Enter your family: ")
national_code = int(input("Enter your national code: "))
hometown = input("Enter your home town(optionl): ")
customer1 = Customer(name, family, national_code, hometown=None)
deposit_amount = int(input("Enter deposit amount: "))
withdraw_amount = int(input("Enter withdraw amount: "))
branch_name = input("Enter the name of the branch: ")
loan_amount = int(input("Enter the amount of loan: "))
bank_id =  int(input("Enter the number of the bank_id(just number): "))
city_name = input("Enter the name of the city_name: ")
number_of_customer = int(input("Enter the number_of_customer: "))
budget = int(input("Enter the budget: "))
balance = int(input("Enter your balance: "))

customer1.get_hometown()


initial_amount = int(input("Enter initial amount: "))
account = customer1.deposit_and_get_account_number(initial_amount)

customer1.deposit(deposit_amount)
customer1.withdraw(withdraw_amount)

customer1.request_loan(branch_name, loan_amount)
branch = Branch(branch_name, bank_id, city_name, number_of_customer, budget)
customer = Customer(name, family, national_code, balance, has_taken_loan=False)
customer.request_loan(branch, loan_amount)




