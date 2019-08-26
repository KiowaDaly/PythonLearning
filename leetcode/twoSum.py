from typing import List


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diction = {}
        for i in range(len(nums)):
            if target-nums[i] not in diction:
                diction[nums[i]] = i
            else:
                return [diction[target - nums[i]], i]


test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
