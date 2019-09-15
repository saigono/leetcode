# https://leetcode.com/problems/count-and-say


class Solution:
    def countAndSay(self, n: int) -> str:
        res = [1]
        for _ in range(n-1):
            new_res = []
            t = 1
            cur_num = res[0]
            cnt = 1
            while t < len(res):
                if res[t] != cur_num:
                    new_res += [cnt, cur_num]
                    cnt = 1
                    cur_num = res[t]
                else:
                    cnt += 1
                t += 1
            if cnt:
                new_res += [cnt, cur_num]
            res = new_res
        return ''.join(str(t) for t in res)