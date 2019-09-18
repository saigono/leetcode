# https://leetcode.com/problems/house-robber
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])

        res = [nums[0], nums[1], max(nums[0] + nums[2], nums[1])]
        i = 3
        while i < len(nums):
            temp = max(
                res[i - 2] + nums[i],
                res[i - 3] + nums[i],
            )
            res.append(temp)
            i += 1
        return max(res[-1], res[-2])
