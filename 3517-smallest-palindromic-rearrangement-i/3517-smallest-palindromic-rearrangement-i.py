from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)

        left = []
        mid = ""

        for c in map(chr, range(ord('a'), ord('z') + 1)):
            left.append(c * (cnt[c] // 2))
            if cnt[c] % 2 == 1:
                mid = c

        left = "".join(left)
        return left + mid + left[::-1]