import unittest
from src.calculator import add, substract, multiply, divide

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3,1), 4, "El resultado no es correcto")

    def test_substract(self):
        self.assertEqual(substract(3,1), 2)
        assert substract(3, 2) == 1

    def test_multipy(self):
        self.assertEqual(multiply(3,2), 6)
        assert multiply(3, 2) == 6

    def test_divide(self):
        self.assertEqual(divide(6,2), 3)
        assert divide(6, 3) == 2

    def test_divitionByZero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)