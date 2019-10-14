# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        
        res = set([''])
        for i in range(n):
            new_res = set()
            for option in res:
                for j in range(len(option) + 1):
                    new_res.add(option[:j] + '()' + option[j:])
            res = new_res
        return res
