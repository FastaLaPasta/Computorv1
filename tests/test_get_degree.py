import unittest
import sys
import os

from get_degree import get_degree

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGetDegree(unittest.TestCase):

    def test_standard_case(self):
        self.assertEqual(get_degree({0: 1, 1: 2, 2: 3}), 2)

    def test_with_zero_coefficients(self):
        self.assertEqual(get_degree({0: 0, 1: 0, 2: 4}), 2)

    def test_all_zero(self):
        # Depends on the way I handle it,
        # If I ignore power for null coefficient then result should be 0
        self.assertEqual(get_degree({0: 0, 1: 0, 2: 0}), 2)

    def test_empty_dict(self):
        self.assertEqual(get_degree({}), 0)

    def test_negative_coefficients(self):
        self.assertEqual(get_degree({0: -1, 2: -5}), 2)

    def test_mixed_zeros_and_nonzeros(self):
        self.assertEqual(get_degree({0: 0, 3: 0, 5: 2}), 5)

    def test_only_constant(self):
        self.assertEqual(get_degree({0: 7}), 0)


if __name__ == '__main__':
    unittest.main()
