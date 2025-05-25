# https://leetcode.com/problems/leaf-similar-trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from itertools import zip_longest

def lrr_iteration(root: Optional[TreeNode]):
    if not root:
        return
    if not root.left and not root.right:
        yield root.val
    yield from lrr_iteration(root.left)
    yield from lrr_iteration(root.right)

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        for (a, b) in zip_longest(lrr_iteration(root1), lrr_iteration(root2)):
            if a != b:
                return False
        return True
