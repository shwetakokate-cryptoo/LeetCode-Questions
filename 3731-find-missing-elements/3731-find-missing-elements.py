from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mn = min(nums)
        mx = max(nums)
        s = set(nums)

        ans = []
        for x in range(mn + 1, mx):
            if x not in s:
                ans.append(x)

        return ans