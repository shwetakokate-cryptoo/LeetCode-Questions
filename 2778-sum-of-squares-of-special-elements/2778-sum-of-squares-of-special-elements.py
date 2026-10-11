
class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            if n % (i + 1) == 0:
                total += nums[i] ** 2

        return total
