
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        diff.sort(reverse=True)
        diff.append(0)

        for i in range(len(diff) - 1):
            need = (i + 1) * (diff[i] - diff[i + 1])

            if k >= need:
                k -= need
            else:
                level, rem = divmod(k, i + 1)
                level = diff[i] - level

                ans = sum(x * x for x in diff[i + 1:])
                ans += rem * (level - 1) ** 2
                ans += (i + 1 - rem) * level ** 2

                return ans

        return 0
