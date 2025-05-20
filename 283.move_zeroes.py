# https://leetcode.com/problems/move-zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_pos = 0
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write_pos] = nums[i]
                write_pos += 1
            else:
                zero_cnt += 1
        for i in range(zero_cnt):
            nums[-1-i] = 0
