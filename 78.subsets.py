# https://leetcode.com/problems/subsets/
# ugly solution

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        level = set([tuple()])
        for i in range(len(nums)):
            new_level = set()
            for s in level:
                for n in nums:
                    if n not in s:
                        new_level.add(tuple(sorted(s + (n, ))))
            level = new_level
            res += [list(x) for x in level]
        return res
