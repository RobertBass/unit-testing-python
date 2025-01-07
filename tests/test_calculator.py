import unittest
from src.calculator import add, substract, multiply, divide

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        assert add(2, 3) == 5

    def test_substract(self):
        assert substract(3, 2) == 1

    def test_multipy(self):
        assert multiply(3, 2) == 6

    def test_divide(self):
        assert divide(6, 3) == 2

    '''def test_divitionByZero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)'''