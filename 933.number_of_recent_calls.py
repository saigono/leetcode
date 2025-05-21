# https://leetcode.com/problems/number-of-recent-calls/description

from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()
        

    def ping(self, t: int) -> int:
        cutoff = 3000
        while self.q and t - self.q[0] > cutoff:
            self.q.popleft()
        self.q.append(t)
        return len(self.q)
