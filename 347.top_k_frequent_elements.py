# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter
from itertools import chain
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        
        inv_freq = {}
        for num, freq in frequencies.items():
            s = inv_freq.setdefault(freq, set())
            s.add(num)
        
        top_freq = chain(*[inv_freq[key] for key in sorted(inv_freq, reverse=True)])
        result = []
        for _ in range(k):
            result.append(next(top_freq))
        return result
