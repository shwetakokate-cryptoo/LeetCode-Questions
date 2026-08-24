from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        ans = stones[-1]

        for i in range(len(stones) - 2, 0, -1):
            ans = max(ans, stones[i] - ans)

        return ans