# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def dfs(root, q, p):
    if not root or root == q or root == p:
        return root

    left = dfs(root.left, q, p)
    right = dfs(root.right, q, p)

    if left and right:
        return root
    
    if left:
        return left
    return right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return dfs(root, p, q)
