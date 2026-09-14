class Solution:
    def mirrorDistance(self, n: int) -> int:
        original = n
        reverse = int(str(n)[::-1])
        return abs(original - reverse)