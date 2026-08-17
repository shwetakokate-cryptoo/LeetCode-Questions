from typing import List
from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        prefix = list(accumulate(stoneValue, initial=0))

        @cache
        def dfs(i, j):
            if i >= j:
                return 0

            ans = 0
            left = 0
            right = prefix[j + 1] - prefix[i]

            for k in range(i, j):
                left += stoneValue[k]
                right -= stoneValue[k]

                if left < right:
                    if ans >= left * 2:
                        continue
                    ans = max(ans, left + dfs(i, k))

                elif left > right:
                    if ans >= right * 2:
                        break
                    ans = max(ans, right + dfs(k + 1, j))

                else:
                    ans = max(
                        ans,
                        left + dfs(i, k),
                        right + dfs(k + 1, j)
                    )

            return ans

        return dfs(0, len(stoneValue) - 1)