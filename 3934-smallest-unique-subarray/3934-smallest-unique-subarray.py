
class Solution:
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        b1, b2 = 100019, 100043
        m1, m2 = 10**9 + 7, 10**9 + 9

        def check(length):
            h1 = h2 = 0
            p1 = pow(b1, length, m1)
            p2 = pow(b2, length, m2)

            freq = {}

            for i in range(length):
                h1 = (h1 * b1 + nums[i]) % m1
                h2 = (h2 * b2 + nums[i]) % m2

            freq[(h1, h2)] = 1

            for i in range(length, n):
                h1 = (h1 * b1 + nums[i] - nums[i - length] * p1) % m1
                h2 = (h2 * b2 + nums[i] - nums[i - length] * p2) % m2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return any(count == 1 for count in freq.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
