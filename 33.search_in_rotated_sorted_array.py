# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 5, 1, 2, 3, 4
        # 2, 3, 4, 5, 1
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        off = l
        l = 0
        r = len(nums) - 1
        while l <= r:
            _mid = (l + r) // 2
            mid = (_mid + off) % len(nums)
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = _mid - 1
            else:
                l = _mid + 1
        return -1
