from typing import List

from pip._vendor.msgpack.fallback import xrange


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        # loop through each index of nums
        # if value != 0 then we swap the values and increase j

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
