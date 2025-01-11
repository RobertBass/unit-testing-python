from src.user import User
from src.bank_account import BankAccount
import unittest, os
from faker import Faker

class UserTest(unittest.TestCase):
    def setUp(self):
        self.faker = Faker(locale="es")
        self.user = User(self.faker.name(), self.faker.email())

    def test_user_creation(self):
        name = self.faker.name()
        email = self.faker.email()
        user = User(name, email)
        self.assertEqual(user.name, name)
        self.assertEqual(user.email, email)

    def test_user_multiple_accounts(self):
        
        for _ in range(3):
            bank_account = BankAccount(
                balance=self.faker.random_int(min=100, max=2000, step=50),
                log_file=self.faker.file_name(extension="txt")
                )
            self.user.addAccount(account=bank_account)
        expected_value = self.user.get_total_balance()
        value = sum(account.get_balance() for account in self.user.accounts)
        self.assertEqual(value, expected_value)

    def tearDown(self) -> None:
        for account in self.user.accounts:
            os.remove(account.log_file)