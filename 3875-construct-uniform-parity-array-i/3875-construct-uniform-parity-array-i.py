class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        has_odd = any(x % 2 for x in nums1)
        has_even = any(x % 2 == 0 for x in nums1)

        if not has_odd or not has_even:
            return True

        return True