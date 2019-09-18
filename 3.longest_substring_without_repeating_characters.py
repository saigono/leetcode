# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        acc = set()  # it can be an array of booleans
        i = 0
        j = 0
        max_len = 0
        while j < len(s):
            while s[j] in acc:
                acc.remove(s[i])
                i += 1
            acc.add(s[j])
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
