# https://leetcode.com/problems/3sum
from typing import List, Tuple


class Solution:
    def threeSum(self, nums: List[int]) -> List[Tuple[int, int, int]]:
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            if nums[i] > 0:
                break
            while j < k:
                t = nums[j] + nums[k]
                if t + nums[i] > 0:
                    k -= 1
                elif t + nums[i] < 0:
                    j += 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
        return list(res)
