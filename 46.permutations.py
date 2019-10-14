# https://leetcode.com/problems/permutations
# This solution is far from great in terms of memory consumption

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = [([], set(nums))]
        
        for i in range(len(nums)):
            new_res = []
            for (p, rest) in res:
                for d in rest:
                    new_res.append((p + [d], rest - {d}))
            res = new_res
        return [x[0] for x in res]
