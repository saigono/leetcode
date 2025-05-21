# https://leetcode.com/problems/unique-number-of-occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnt = defaultdict(int)
        for x in arr:
            cnt[x] += 1
        return len(cnt) == len(set(cnt.values()))
