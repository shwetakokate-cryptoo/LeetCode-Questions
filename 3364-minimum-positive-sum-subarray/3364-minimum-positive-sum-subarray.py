
class Solution:
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        for length in range(l, r + 1):
            total = sum(nums[:length])

            if total > 0:
                ans = min(ans, total)

            for i in range(length, n):
                total += nums[i] - nums[i - length]

                if total > 0:
                    ans = min(ans, total)

        return -1 if ans == float('inf') else ans
