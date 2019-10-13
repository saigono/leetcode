# https://leetcode.com/problems/binary-tree-preorder-traversal/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        s = [root]
        result = []
        while s:
            node = s.pop(-1)
            result.append(node.val)
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return result
