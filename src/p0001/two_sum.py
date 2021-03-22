from typing import List, Dict

__all__ = [
    "Solution"
]


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cache: Dict[int, int] = {}

        i = 0
        while i < len(nums):
            diff = target - nums[i]
            if diff in cache:
                return [cache[diff], i]
            cache[nums[i]] = i
            i += 1

        return [-1, -1]
