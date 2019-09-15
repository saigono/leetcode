# https://leetcode.com/problems/longest-common-prefix


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''

        i = 0
        while True:
            if i >= len(strs[0]):
                return strs[0][:i]
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    return s[:i]
            i += 1
