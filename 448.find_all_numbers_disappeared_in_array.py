# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i, x in enumerate(nums) if x > 0]
