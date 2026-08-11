from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                s += nums[i]
            else:
                break

        x = s
        seen = set(nums)

        while x in seen:
            x += 1

        return x