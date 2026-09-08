class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        return max(0, n - 999) + max(0, n - 999999) + max(0, n - 999999999)