import unittest
from maths import Maths


class MathsUnitest(unittest.TestCase):

    def setUp(self) -> None:
        self.math_obj = Maths(2, 5)

    def test_sum(self):
        expected_sum = 7
        executed_sum = self.math_obj.sum()
        self.assertEqual(executed_sum, expected_sum)

    def test_multiply(self):
        expected_mult = 10
        executed_sum = self.math_obj.mult()
        self.assertEqual(executed_sum, expected_mult)

    def test_sub(self):
        expected_sub = -3
        executed_sub = self.math_obj.sub()
        self.assertEqual(executed_sub, expected_sub)


if __name__ == '__main__':
    unittest.main()
