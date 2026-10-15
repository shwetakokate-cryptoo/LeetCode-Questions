
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            s = set()

            for j in range(i, n):
                s.add(nums[j])
                ans += len(s) ** 2

        return ans
