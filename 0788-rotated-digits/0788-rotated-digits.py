class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0

        for num in range(1, n + 1):
            s = str(num)

            if any(ch in '347' for ch in s):
                continue

            if any(ch in '2569' for ch in s):
                ans += 1

        return ans