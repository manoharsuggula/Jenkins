#!/usr/bin/python3
import unittest

from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_number1(self):
        data = 6
        result = factorial(data)
        self.assertEqual(result, 720)

    def test_number2(self):
        data = 5
        result = factorial(data)
        self.assertEqual(result, 125)

    def test_number3(self):
        data = 4
        result = factorial(data)
        self.assertEqual(result, 24)

if __name__ == '__main__':
    unittest.main()
