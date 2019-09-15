# https://leetcode.com/problems/validate-binary-search-tree


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """Tree is a valid Binary Search Tree, if sequence gathered from Left-Root-Right traversal is sorted"""
        if not root:
            return True

        iterator = self.traverse(root)
        previous_key = next(iterator)
        for key in iterator:
            if key <= previous_key:
                return False
            previous_key = key
        return True

    def traverse(self, node: TreeNode):
        """Traverse tree in Left-Root-Right order"""
        if node.left:
            yield from self.traverse(node.left)
        yield node.val
        if node.right:
            yield from self.traverse(node.right)
