from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        zeros = 0

        for x in nums:
            xor ^= x
            if x == 0:
                zeros += 1

        if xor != 0:
            return n

        if zeros == n:
            return 0

        return n - 1