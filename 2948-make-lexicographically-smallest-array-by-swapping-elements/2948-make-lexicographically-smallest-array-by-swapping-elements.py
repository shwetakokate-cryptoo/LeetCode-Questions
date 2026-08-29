from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = [0] * n

        i = 0

        while i < n:
            j = i + 1

            while j < n and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1

            indices = sorted(idx for _, idx in arr[i:j])

            for idx, (value, _) in zip(indices, arr[i:j]):
                ans[idx] = value

            i = j

        return ans