# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from bisect import bisect, bisect_left
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        a = bisect_left(nums, target)
        b = bisect(nums, target)
        if a == b:
            return [-1, -1]
        
        return [a, b - 1]
