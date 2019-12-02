# https://leetcode.com/problems/combination-sum/

from bisect import bisect_left
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = self._combinationSum(sorted(candidates), target, [])
        return list(result)
    
    def _combinationSum(self, candidates: List[int], target: int, track: List[int]):
        i = bisect_left(candidates, track[-1]) if track else 0
        for c in candidates[i:]:
            if c == target:
                track.append(c)
                yield tuple(track)
                track.pop(-1)
            elif c < target:
                track.append(c)
                yield from self._combinationSum(candidates, target - c, track)
                track.pop(-1)
            else:
                break
