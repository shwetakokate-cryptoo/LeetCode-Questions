class Solution:
    def minMoves(self, nums):
        return sum(nums) - min(nums) * len(nums)