# https://leetcode.com/problems/same-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    def isSameTreeIterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            l, r = stack.pop()
            if l is None and r is None:
                continue

            if l is None or r is None or l.val != r.val:
                return False

            stack.append([l.left, r.left])
            stack.append([l.right, r.right])
        return True
