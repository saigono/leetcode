# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraversal(self, root: Optional[TreeNode]):
        if root.left:
            yield from self.inOrderTraversal(root.left)
        yield root.val
        if root.right:
            yield from self.inOrderTraversal(root.right)
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversal = self.inOrderTraversal(root)
        for _ in range(k-1):
            next(traversal)
        return next(traversal)
