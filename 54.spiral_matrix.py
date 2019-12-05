# https://leetcode.com/problems/spiral-matrix/
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        left = 0
        top = 0
        
        result = []
        size = len(matrix) * len(matrix[0])
        while len(result) < size:
            result.extend(matrix[top][left:right + 1])
            if len(result) >= size:
                break
            for j in range(top + 1, bottom + 1):
                result.append(matrix[j][right])
            if len(result) >= size:
                break
            for i in range(right - 1, left -1, -1):
                result.append(matrix[bottom][i])
            if len(result) >= size:
                break
            for j in range(bottom - 1, top, -1):
                result.append(matrix[j][left])
            
            right -= 1
            bottom -= 1
            left += 1
            top += 1
        return result
