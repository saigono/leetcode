# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for n in nums[1:]:
            max_sum = max(cur_sum, max_sum)
            if cur_sum < 0:
                cur_sum = n
            else:
                cur_sum += n
        return max(cur_sum, max_sum)
