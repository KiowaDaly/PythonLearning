from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for i in nums:
            r ^= i
        return r