import unittest
from two_sum import Solution as TwoSumSolution


class TestStringMethods(unittest.TestCase):

    def test_001(self):
        result = TwoSumSolution().twoSum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])


if __name__ == '__main__':
    unittest.main()
