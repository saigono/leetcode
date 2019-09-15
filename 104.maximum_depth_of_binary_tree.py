# https://leetcode.com/problems/maximum-depth-of-binary-tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(1, root)]
        max_depth = 0
        while stack:
            depth, node = stack.pop(0)
            if node.left:
                stack.insert(0, (depth + 1, node.left))
            if node.right:
                stack.insert(0, (depth + 1, node.right))
            max_depth = max(depth, max_depth)
        return max_depth
