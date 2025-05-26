# https://leetcode.com/problems/binary-tree-right-side-view
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([(root, 0)])
        result = [None for _ in range(100)] # max number of nodes
        while q:
            node, h = q.popleft()
            if not node:
                continue
            result[h] = node.val
            q.append((node.left, h+1))
            q.append((node.right, h+1))

        return [x for x in result if x is not None]
