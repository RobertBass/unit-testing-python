import pytest
from src.bank_account import BankAccount

def test_sum():
    a = 4
    b = 4
    assert a + b == 8

@pytest.mark.parametrize("amount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500)
])
def test_deposit_many_ammounts(amount, expected):
    account = BankAccount(1000, "transactions.txt")
    account.get_balance()
    assert account.deposit(amount) == expected