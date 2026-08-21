from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        subsets = []

        for mask in range(1, 1 << n):
            lcm = 1
            bits = 0

            for i in range(n):
                if mask & (1 << i):
                    bits += 1
                    lcm = lcm * coins[i] // gcd(lcm, coins[i])

                    if lcm > k * min(coins):
                        break

            if lcm <= k * min(coins):
                subsets.append((lcm, bits))

        def count(x):
            total = 0

            for lcm, bits in subsets:
                if bits % 2:
                    total += x // lcm
                else:
                    total -= x // lcm

            return total

        left = 1
        right = k * min(coins)

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left