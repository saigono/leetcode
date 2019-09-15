# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree
from typing import List


class TreeNode:
    def __init__(self, x):
        """ Definition for a binary tree node."""
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        n_2 = len(nums) // 2
        root = TreeNode(nums[n_2])
        root.left = self.sortedArrayToBST(nums[:n_2])
        root.right = self.sortedArrayToBST(nums[n_2 + 1:])
        return root
