class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self.log_transaction(f'ACCOUNT CREATED SUCCESFULLY')
    
    def log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f"{message}\n")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.log_transaction(f"AMOUNT OF DEPOSIT: {amount}. NEW BALANCE: {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount > 0:
            if amount < self.balance:
                self.balance -= amount
                self.log_transaction(f"AMOUNT OF WITHDRAW: {amount}. NEW BALANCE: {self.balance}")
            else:
                return self.log_transaction(f"INSUFFICIENT FUNDS. BALANCE: {self.balance}")
        return self.balance

    
    def get_balance(self):
        self.log_transaction(f"CHECKED BALANCE. CURRENT BALANCE: {self.balance}")
        return self.balance