import unittest
import sys
import os

from solve import solve

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestSolve(unittest.TestCase):

    def test_degree_0_all_zero(self):
        self.assertEqual(solve({}), "Any real number is a solution.")

    def test_degree_0_non_zero(self):
        self.assertEqual(solve({0: 5}), "No solution.")

    def test_degree_1_normal(self):
        self.assertEqual(solve({1: 2, 0: -4}), "The solution is:\n2.0")

    def test_degree_1_zero_coeff(self):
        self.assertEqual(solve({1: 0, 0: 5}), "No solution.")

    def test_degree_2_two_real_solutions(self):
        result = solve({2: 1, 1: -3, 0: 2})
        self.assertTrue(result.startswith("Discriminant is strictly positive, the two solutions are"))
        parts = result.split("\n")
        self.assertEqual(len(parts), 3)
        self.assertAlmostEqual(float(parts[1]), 1.0)
        self.assertAlmostEqual(float(parts[2]), 2.0)

    def test_degree_2_one_real_solution(self):
        result = solve({2: 1, 1: -2, 0: 1})
        self.assertEqual(result, "The solution is:\n1.0")

    def test_degree_2_complex_solutions(self):
        result = solve({2: 1, 1: 2, 0: 5})
        self.assertTrue(result.startswith("Discriminant is strictly negative, the two complex solutions are:"))
        self.assertIn("i", result)
        parts = result.split("\n")
        self.assertEqual(len(parts), 3)
        self.assertIn("i", parts[1])
        self.assertIn("i", parts[2])


if __name__ == "__main__":
    unittest.main()
