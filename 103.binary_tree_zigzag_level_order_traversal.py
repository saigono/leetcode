# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [(root, 1)]
        result = defaultdict(list)
        
        while q:
            node, level = q.pop(0)
            if level % 2:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
                
        real_result = []
        for k in sorted(result):
            real_result.append(result[k])
        return real_result
