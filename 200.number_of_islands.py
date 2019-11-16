# https://leetcode.com/problems/number-of-islands/

from collections import deque
from typing import List

class Solution:
    @staticmethod
    def color(grid: List[List[str]], i: int, j: int, c: str):
        q = deque([(i, j)])
        while q:
            i, j = q.popleft()
            if grid[i][j] != '1':
                continue
            grid[i][j] = c
            if i > 0:
                q.append((i-1, j))
            if i + 1 < len(grid):
                q.append((i+1, j))
            if j > 0:
                q.append((i, j-1))
            if j + 1 < len(grid[i]):
                q.append((i, j+1))
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        cur_color = 2
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.color(grid, i, j, str(cur_color))
                    cur_color += 1
        
        return cur_color - 2
