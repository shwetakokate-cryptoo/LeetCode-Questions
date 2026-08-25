from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)

        x = k
        while x in seen:
            x += k

        return x