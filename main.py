from src.customer import Customer

name = input("Enter your name: ")
family = input("Enter your family: ")
national_code = int(input("Enter your national code: "))
hometown = input("Enter your home town(optionl): ")
customer1 = Customer(name, family, national_code, hometown=None)
customer1.get_hometown()
