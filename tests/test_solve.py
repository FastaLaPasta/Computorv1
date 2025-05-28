import unittest
import sys
import os

from solve import solve

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestSolve(unittest.TestCase):

    def test_degree_0_all_zero(self):
        self.assertEqual(solve({}), "All real numbers are solutions.")

    def test_degree_0_non_zero(self):
        self.assertEqual(solve({0: 5}), "No solution.")

    def test_degree_1_normal(self):
        self.assertEqual(solve({1: 2, 0: -4}), 2.0)

    def test_degree_1_zero_coeff(self):
        self.assertEqual(solve({1: 0, 0: 5}), "No solution.")

    def test_degree_2_two_real_solutions(self):
        result = solve({2: 1, 1: -3, 0: 2})
        self.assertIn("Two real solutions", result)
        self.assertIn("x1 =", result)
        self.assertIn("x2 =", result)

    def test_degree_2_one_real_solution(self):
        result = solve({2: 1, 1: -2, 0: 1})
        self.assertIn("One real solution", result)
        self.assertIn("x =", result)

    def test_degree_2_complex_solutions(self):
        result = solve({2: 1, 1: 2, 0: 5})
        self.assertIn("Two complex solutions", result)
        self.assertIn("i", result)


if __name__ == "__main__":
    unittest.main()
