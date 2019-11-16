# https://leetcode.com/problems/decode-string/

def calculate_string(s, pos):
    result = ''
    n = len(s)
    while pos < n and s[pos] != ']':
        c = s[pos]
        if c.isdigit():
            t = int(c)
            pos += 1
            while s[pos].isdigit():
                t = t*10 + int(s[pos])
                pos += 1
            
            pos, sub = calculate_string(s, pos + 1)
            result = result + t * sub
        else:
            result = result + c
            pos += 1
    return pos + 1, result
        
class Solution:
    def decodeString(self, s: str) -> str:
        _, sub = calculate_string(s, 0)
        return sub
