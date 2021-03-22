# https://leetcode.com/problems/fizz-buzz/
from typing import List


class Solution:
    def fizzBuzz(self, n: int):
        _list: List[str] = []
        i: int = 1
        while i <= n:
            if i % 3 == 0:
                if i % 5 == 0:
                    _list.append("FizzBuzz")
                else:
                    _list.append("Fizz")
            else:
                if i % 5 == 0:
                    _list.append("Buzz")
                else:
                    _list.append(str(i))
            i += 1

        return _list
