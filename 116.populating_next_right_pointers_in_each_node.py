# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        s = [root]
        while s:
            new_s = []
            node = s.pop(0)
            if node.left:
                new_s.append(node.left)
                new_s.append(node.right)
            while s:
                rnode = s.pop(0)
                node.next = rnode
                node = rnode
                if node.left:
                    new_s.append(node.left)
                    new_s.append(node.right)
            s = new_s
        return root
