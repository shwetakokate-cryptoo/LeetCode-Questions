
class Solution:
    def sortPermutation(self, nums):
        ans = -1

        for i in range(len(nums)):
            if nums[i] != i:
                ans &= nums[i]

        return max(ans, 0)
