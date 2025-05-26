# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        st = [(root, 0, None)]
        max_zz = 0
        while st:
            node, cur_zz, direction = st.pop()
            if not node:
                continue
            max_zz = max(max_zz, cur_zz)
            st.append((node.left, cur_zz + 1 if direction != 'l' else 1, 'l'))
            st.append((node.right, cur_zz + 1 if direction != 'r' else 1, 'r'))
        return max_zz
