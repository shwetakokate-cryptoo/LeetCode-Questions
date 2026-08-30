class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        min_i = nums.index(min(nums))
        max_i = nums.index(max(nums))

        a = min(min_i, max_i) + 1
        b = max(min_i, max_i) + 1

        return min(
            b,
            n - a + 1,
            a + n - b + 1
        )