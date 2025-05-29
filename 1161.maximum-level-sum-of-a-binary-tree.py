# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = [root] if root else []
        min_level = 1
        cur_level = 1
        max_sum = float("-inf")
        while level:
            new_level = []
            cur_sum = 0
            for node in level:
                cur_sum += node.val
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            if cur_sum > max_sum:
                min_level = cur_level
                max_sum = cur_sum
            level = new_level
            cur_level += 1

        return min_level
                
