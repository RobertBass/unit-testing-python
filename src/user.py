class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def addAccount(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)
