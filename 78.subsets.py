# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        while nums:
            n = nums.pop(0)
            res += [x + [n] for x in res]
        return res
