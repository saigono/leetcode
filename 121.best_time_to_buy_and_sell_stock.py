# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_values = [prices[-1]]
        cur_max = prices[-1]
        for val in prices[::-1][:-1]:
            cur_max = max(val, cur_max)
            max_values.append(cur_max)
        max_values = max_values[::-1]
        profit = 0
        for i, val in enumerate(prices[:-1]):
            profit = max(profit, max_values[i] - val)
        return profit
