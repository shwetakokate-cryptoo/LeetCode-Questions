
class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        pref_max = [0] * (n + 1)
        suff_min = [float('inf')] * (n + 1)
        drops = [0] * n

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(suff_min[i + 1], nums[i])

        for i in range(1, n):
            drops[i] = drops[i - 1] + (nums[i - 1] > nums[i])

        ans = 0

        for k in range(1, n + 1):
            if n % k:
                continue

            valid = True

            for start in range(0, n, k):
                end = start + k - 1
                internal_drops = drops[end] - drops[start]
                circular_drop = nums[end] > nums[start]

                if internal_drops + circular_drop > 1:
                    valid = False
                    break

                if pref_max[start] > suff_min[start]:
                    valid = False
                    break

            if valid:
                ans += k

        return ans
