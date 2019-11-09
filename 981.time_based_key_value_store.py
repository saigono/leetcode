# https://leetcode.com/problems/time-based-key-value-store/

from bisect import bisect
from collections import defaultdict


class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._timestamps = defaultdict(list)
        self._data = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._timestamps[key].append(timestamp)
        self._data[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect(self._timestamps[key], timestamp) - 1
        if idx < 0:
            return ''
        else:
            return self._data[key][idx]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
