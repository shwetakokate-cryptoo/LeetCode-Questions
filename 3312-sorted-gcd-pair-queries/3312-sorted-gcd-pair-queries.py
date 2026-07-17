from typing import List
from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        # Frequency of each value
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        # Count numbers divisible by i
        div_count = [0] * (mx + 1)
        for i in range(1, mx + 1):
            for j in range(i, mx + 1, i):
                div_count[i] += freq[j]

        # exact[g] = number of pairs with gcd exactly g
        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            c = div_count[g]
            pairs = c * (c - 1) // 2
            m = 2 * g
            while m <= mx:
                pairs -= exact[m]
                m += g
            exact[g] = pairs

        # Prefix sums of pair counts
        prefix = []
        values = []
        total = 0
        for g in range(1, mx + 1):
            if exact[g]:
                total += exact[g]
                prefix.append(total)
                values.append(g)

        # Answer queries
        ans = []
        for q in queries:
            idx = bisect_left(prefix, q + 1)
            ans.append(values[idx])

        return ans