import unittest, os
from unittest.mock import patch
from src.Exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount

# RUN "python -m unittest path" in terminal

class BankAccountTest(unittest.TestCase):
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, 'r') as f:
            return len(f.readlines())
        

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500
    
    @patch("src.bank_account.datetime")
    def test_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        new_balance = self.account.withdraw(300)
        assert new_balance == 700

    @patch("src.bank_account.datetime")
    def test_over_withdraw(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(1200)

    def test_getBalance(self):
        assert self.account.get_balance() == 1000
        
    def test_transaction_log(self):
        self.account.deposit(500)
        assert os.path.exists("transaction_log.txt")

    def test_count_transactions(self):
        assert self._count_lines(self.account.log_file) == 1
        self.account.deposit(500)
        assert self._count_lines(self.account.log_file) == 2

    @patch("src.bank_account.datetime")
    def test_withdraw_during_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        self.assertEqual(self.account.withdraw(100), 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_before_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_after_bussines_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    def test_deposit_many_ammounts(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4100},
            {"amount": 4500, "expected": 8600},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.assertEqual(self.account.deposit(case["amount"]), case["expected"])
