# https://leetcode.com/problems/course-schedule-ii/
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = [set() for _ in range(numCourses)]
        nei = [set() for _ in range(numCourses)]
        
        for (t, f) in prerequisites:
            req[t].add(f)  # stores requirements for course t
            nei[f].add(t)  # stores courses, that require course f
            
        result = []
        
        # stack with all courses without requirements
        s = [i for i, dep in enumerate(req) if not dep]
        
        
        while s:
            node = s.pop(-1)
            for n in nei[node]:
                # we visited one of the course n requirements, removing it
                req[n].remove(node)
                if not req[n]:
                    # if there are no requirements left for n, it can be added to stack
                    s.append(n)
            # since node is from stack, it means that all requirements has been satisfied
            # we can add this node to the result
            result.append(node)
            
        return [] if len(result) < numCourses else result
