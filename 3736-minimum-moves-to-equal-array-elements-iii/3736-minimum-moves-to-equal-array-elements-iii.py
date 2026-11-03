class Solution:
    def minMoves(self, nums):
        maximum = max(nums)
        return maximum * len(nums) - sum(nums)