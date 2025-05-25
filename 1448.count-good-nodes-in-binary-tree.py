# https://leetcode.com/problems/count-good-nodes-in-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_goods = 0
        s = deque()
        s.append((root, root.val))
        while s:
            node, cur_max = s.pop()
            
            if node.val >= cur_max:
                num_goods += 1
            
            if node.left:
                s.append((node.left, max(cur_max, node.val)))

            if node.right:
                s.append((node.right, max(cur_max, node.val)))
        
        return num_goods
