
class Solution:
    def minOperations(self, nums):
        dranofelik = nums[:]
        n = len(dranofelik)
        zero = dranofelik.index(0)

        def check(step):
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n

                if dranofelik[prev] > dranofelik[curr]:
                    return False

            return True

        ans = float('inf')

        if check(1):
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)

        if check(-1):
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)

        return -1 if ans == float('inf') else ans
