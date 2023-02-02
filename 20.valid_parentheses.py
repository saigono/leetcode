# https://leetcode.com/problems/valid-parentheses/

from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c in '({[':
                stack.appendleft(c)
            else:
                if not stack:
                    return False
                k = stack.popleft()
                if c == ')' and k != '(':
                    return False
                elif c == ']' and k != '[':
                    return False
                elif c == '}' and k != '{':
                    return False
        return not stack
