import unittest
from power_of_two import Solution


class SolutionTest(unittest.TestCase):

    def test_001(self):
        
        self.assertFalse(Solution().isPowerOfTwo(-1))
        self.assertFalse(Solution().isPowerOfTwo(0))
        self.assertFalse(Solution().isPowerOfTwo(3))

        self.assertTrue(Solution().isPowerOfTwo(1))
        self.assertTrue(Solution().isPowerOfTwo(2))
        self.assertTrue(Solution().isPowerOfTwo(4))


if __name__ == '__main__':
    unittest.main()
