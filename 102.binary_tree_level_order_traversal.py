# https://leetcode.com/problems/binary-tree-level-order-traversal
from typing import List


class TreeNode:
    def __init__(self, x):
        """ Definition for a binary tree node."""
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        level = [root]
        result = []
        while level:
            result.append([x.val for x in level])
            new_level = []
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level
        return result
