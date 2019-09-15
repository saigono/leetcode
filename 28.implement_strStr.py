# https://leetcode.com/problems/implement-strstr/


class Solution:
    @staticmethod
    def build_z_function(s):
        z = [0 for _ in s]
        i = 1
        l = 0
        r = 0
        while i < len(s):
            if i <= r:
                z[i] = min(r - i + 1, z[i-l])
            while i + z[i] < len(s) and s[z[i]] == s[i+z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
            i += 1
        return z

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        z = self.build_z_function(f'{needle}${haystack}')
        for i, x in enumerate(z):
            if x == len(needle):
                return i - x - 1
        return -1