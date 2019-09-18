# https://leetcode.com/problems/count-primes
from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        return sum(self.sieve(n))

    def sieve(self, n: int) -> List[int]:
        sieve = [True] * n
        sieve[0] = sieve[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            for j in range(i * i, n, i):
                sieve[j] = False
        return sieve
