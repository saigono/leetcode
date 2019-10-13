# https://leetcode.com/problems/binary-tree-inorder-traversal

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s = []
        res = []
        node = root
        while node or s:
            while node:
                s.append(node)
                node = node.left
            node = s.pop(-1)
            res.append(node.val)
            node = node.right
        return res
