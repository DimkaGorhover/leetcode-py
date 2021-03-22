import math


class Solution:
    def reverse(self, x: int) -> int:

        if abs(x) < 10:
            return x

        max = 2 ** 31
        input: int = abs(x)
        output: int = 0

        while input > 0:
            output = (output * 10) + (input % 10)
            input = math.floor(input / 10)
            if output > max:
                return 0

        if x < 0:
            return 0 - output

        return output


print(F"       123 = {Solution().reverse(123):4}")
print(F"      -123 = {Solution().reverse(-123):4}")
print(F"1534236469 = {Solution().reverse(1_534_236_469):4}")
