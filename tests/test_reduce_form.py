import unittest
import sys
import os

from reduce_form import reduce_form
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


if __name__ == "__main__":
    unittest.main()
