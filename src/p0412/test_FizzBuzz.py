from unittest import TestCase

from FizzBuzz import Solution


class TestSolution(TestCase):
    def test_fizz_buzz(self):
        actual = Solution().fizzBuzz(15)
        expected = ['1', '2', 'Fizz', '4', 'Buzz',
                    'Fizz', '7', '8', 'Fizz', 'Buzz',
                    '11', 'Fizz', '13', '14', 'FizzBuzz']
        self.assertEqual(expected, actual)
