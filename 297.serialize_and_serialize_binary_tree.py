# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        stack = deque([root])
        while stack:
            new_stack = deque()
            while stack:
                node = stack.popleft()
                if node is None:
                    result.append(None)
                else:
                    new_stack.append(node.left)
                    new_stack.append(node.right)
                    result.append(node.val)
            if not any(new_stack):
                break
            stack = new_stack

        return ','.join(str(x) if x is not None else 'x' for x in result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = deque(int(x) if x != 'x' else None for x in data.split(','))
        if not data:
            return None
        root_data = data.popleft()
        if root_data is None:
            return None
        root = TreeNode(root_data)
        parents = [root]
        while data:
            new_parents = []
            for parent in parents:
                if parent is None:
                    continue
                left = data.popleft()
                right = data.popleft()
                if left is not None:
                    left = TreeNode(left)
                if right is not None:
                    right = TreeNode(right)
                new_parents.append(left)
                new_parents.append(right)
                parent.left = left
                parent.right = right
            parents = new_parents
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
