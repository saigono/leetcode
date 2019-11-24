# https://leetcode.com/problems/merge-intervals/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        timeline = []
        for (begin, end) in intervals:
            timeline.append((begin, 0))
            timeline.append((end, 1))
        
        timeline.sort()
        
        stack = []
        for (value, bracket) in timeline:
            if not bracket:
                stack.append((value, bracket))
            else:
                v, b = stack.pop(-1)
                if not b:
                    if not stack:
                        result.append([v, value])                        
                else:
                    while stack:
                        v, b = stack.pop(-1)
                    result.append([v, value])
        return result
