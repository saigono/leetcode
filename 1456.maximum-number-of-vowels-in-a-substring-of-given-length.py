# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = min(len(s), k)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_v = sum(c in vowels for c in s[l:r])
        cur_v = max_v
        l += 1
        r += 1
        while r <= len(s):
            cur_v = cur_v - (s[l-1] in vowels) + (s[r-1] in vowels)
            max_v = max(cur_v, max_v)
            l += 1
            r += 1
        return max_v
