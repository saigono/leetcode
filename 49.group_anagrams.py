# https://leetcode.com/problems/group-anagrams

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The key could be a tuple with letters count. Too lazy to implement it
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)
        return d.values()
