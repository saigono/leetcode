# https://leetcode.com/problems/symmetric-tree

class TreeNode:
    def __init__(self, x):
        """Definition for a binary tree node."""
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        it1 = self.left_root_right_traversal(root)
        it2 = self.right_root_left_traversal(root)
        n1 = next(it1)
        n2 = next(it2)
        while n1 != (root.val, 0) and n2 != (root.val, 0):
            if n1 != n2:
                return False
            n1 = next(it1)
            n2 = next(it2)
        return n1 == n2

    def left_root_right_traversal(self, node: TreeNode, depth: int = 0):
        if not node:
            return
        yield from self.left_root_right_traversal(node.left, depth + 1)
        yield (node.val, depth)
        yield from self.left_root_right_traversal(node.right, depth + 1)

    def right_root_left_traversal(self, node: TreeNode, depth: int = 0):
        if not node:
            return
        yield from self.right_root_left_traversal(node.right, depth + 1)
        yield (node.val, depth)
        yield from self.right_root_left_traversal(node.left, depth + 1)


class SolutionIterative:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        left_subtree = [root.left]
        right_subtree = [root.right]
        while left_subtree and right_subtree:
            if [x.val if x else None for x in left_subtree] != [x.val if x else None for x in reversed(right_subtree)]:
                return False
            new_left_subtree = []
            for node in left_subtree:
                if not node:
                    continue
                new_left_subtree += [node.left, node.right]
            left_subtree = new_left_subtree
            new_right_subtree = []
            for node in right_subtree:
                if not node:
                    continue
                new_right_subtree += [node.left, node.right]
            right_subtree = new_right_subtree

        return not left_subtree and not right_subtree
