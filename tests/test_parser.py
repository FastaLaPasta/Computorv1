import unittest
import sys
import os

from parse import parse_equation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestParseEquation(unittest.TestCase):

    def test_simple_polynomial(self):
        expr = "3 * x^2 + 2 * x^1 + 2 * x^0"
        expected = {2: 3.0, 1: 2.0, 0: 2.0}
        self.assertEqual(parse_equation(expr), expected)

    def test_with_negative_terms(self):
        expr = "3 * x^2 - 2 * x^1 + 1 * x^0"
        expected = {2: 3.0, 1: -2.0, 0: 1.0}
        self.assertEqual(parse_equation(expr), expected)

    def test_missing_coefficient(self):
        expr = "x^2 + x + 1"
        expected = {2: 1.0, 1: 1.0, 0: 1.0}
        self.assertEqual(parse_equation(expr), expected)

    def test_negative_signs_and_whitespace(self):
        expr = "-3*x^2 + 2*x^1 - 5*x^0"
        expected = {2: -3.0, 1: 2.0, 0: -5.0}
        self.assertEqual(parse_equation(expr), expected)

    def test_constant_only(self):
        expr = "5"
        expected = {0: 5.0}
        self.assertEqual(parse_equation(expr), expected)

    def test_no_spaces_or_multiplications(self):
        expr = "4x^2+3x^1+1"
        expected = {2: 4.0, 1: 3.0, 0: 1.0}
        self.assertEqual(parse_equation(expr), expected)


if __name__ == "__main__":
    unittest.main()
