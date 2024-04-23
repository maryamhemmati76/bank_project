class Bank:
    def __init__(self, name, bank_id,  /, *args, **kwargs):
        self.name = name
        self.bank_id = bank_id

    def show_details(self):
        print(f"Name: {self.name}, Bank ID: {self.bank_id}")