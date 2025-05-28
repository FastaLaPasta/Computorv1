import unittest
import sys
import os

from reduce_form import reduce_form, format_reduced_form
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestReduceForm(unittest.TestCase):

    def test_basic(self):
        left = {2: 3.0, 1: 2.0, 0: 2.0}
        right = {0: 1.0}
        result = reduce_form(left.copy(), right)
        self.assertEqual(result, {2: 3.0, 1: 2.0, 0: 1.0})

    def test_with_new_exponent(self):
        left = {2: 3.0}
        right = {1: 1.0}
        result = reduce_form(left.copy(), right)
        self.assertEqual(result, {2: 3.0, 1: -1.0})

    def test_all_same(self):
        left = {0: 4.0}
        right = {0: 4.0}
        result = reduce_form(left.copy(), right)
        self.assertEqual(result, {0: 0.0})

    def test_negative_result(self):
        left = {1: 1.0}
        right = {1: 3.0}
        result = reduce_form(left.copy(), right)
        self.assertEqual(result, {1: -2.0})

    def test_empty_right(self):
        left = {2: 5.0}
        right = {}
        result = reduce_form(left.copy(), right)
        self.assertEqual(result, {2: 5.0})


class TestFormatReduceForm(unittest.TestCase):
    def test_standard_equation(self):
        self.assertEqual(
            format_reduced_form({2: 3, 1: -2, 0: -5}),
            "Reduced form: 3 * x^2 - 2 * x - 5 = 0"
        )

    def test_missing_terms(self):
        self.assertEqual(
            format_reduced_form({2: 3, 0: 5}),
            "Reduced form: 3 * x^2 + 5 = 0"
        )

    def test_negative_coefficients(self):
        self.assertEqual(
            format_reduced_form({2: -1, 1: -2, 0: -3}),
            "Reduced form: -1 * x^2 - 2 * x - 3 = 0"
        )

    def test_zero_coefficients(self):
        self.assertEqual(
            format_reduced_form({2: 0, 1: 4, 0: 0}),
            "Reduced form: 4 * x = 0"
        )

    def test_all_zero_coefficients(self):
        self.assertEqual(
            format_reduced_form({2: 0, 1: 0, 0: 0}),
            "Reduced form: 0 = 0"
        )

    def test_single_constant_term(self):
        self.assertEqual(
            format_reduced_form({0: 7}),
            "Reduced form: 7 = 0"
        )

    def test_single_linear_term(self):
        self.assertEqual(
            format_reduced_form({1: -1}),
            "Reduced form: -1 * x = 0"
        )

    def test_single_quadratic_term(self):
        self.assertEqual(
            format_reduced_form({2: 2}),
            "Reduced form: 2 * x^2 = 0"
        )

    def test_spacing_and_signs(self):
        self.assertEqual(
            format_reduced_form({2: 1, 1: 1, 0: 1}),
            "Reduced form: 1 * x^2 + 1 * x + 1 = 0"
        )
        self.assertEqual(
            format_reduced_form({2: -1, 1: 1, 0: -1}),
            "Reduced form: -1 * x^2 + 1 * x - 1 = 0"
        )


if __name__ == "__main__":
    unittest.main()
