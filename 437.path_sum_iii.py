# https://leetcode.com/problems/path-sum-iii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        psum_counter = 0
        st = [(root, 0, {0: 1})]
        while st:
            node, current_sum, prefix_cache = st.pop()
            if not node:
                continue
            current_sum += node.val
            psum_counter += prefix_cache.get(current_sum - targetSum, 0)
            prefix_cache[current_sum] = prefix_cache.get(current_sum, 0) + 1
            st.append((node.left, current_sum, prefix_cache.copy()))
            st.append((node.right, current_sum, prefix_cache.copy()))
        return psum_counter
