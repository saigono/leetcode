# https://leetcode.com/problems/kth-largest-element-in-an-array/

from random import choice
from typing import List

class Solution:
    @staticmethod
    def _partition(arr, l, r):
        mid = (l + r) // 2
        pivot_idx = choice((l, r, mid))
        
        pivot = arr[pivot_idx]
        arr[l], arr[pivot_idx] = arr[pivot_idx], arr[l]

        for i in range(l, r + 1):
            if arr[i] > pivot:
                arr[i], arr[l], arr[l+1] = arr[l+1], arr[i], arr[l]
                l += 1
        
        return l
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        while True:
            pos = self._partition(nums, l, r)
            if pos + 1 == k:
                return nums[pos]
            elif pos + 1 > k:
                r = pos
            else:
                l = pos + 1
