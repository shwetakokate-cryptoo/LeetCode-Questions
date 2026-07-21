class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Number of active sections initially.
        active = s.count("1")

        # Add the augmented 1's at both ends.
        t = "1" + s + "1"
        n = len(t)

        # Run-length encoding of t.
        runs = []  # (character, length)
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        # Maximum increase in active sections after one trade.
        max_gain = 0

        # A valid trade requires a block of 1's surrounded by 0's.
        # If we have: ... 0^(a) 1^(b) 0^(c) ...
        # the net gain is a + c.
        for i in range(1, len(runs) - 1):
            if (
                runs[i][0] == "1"
                and runs[i - 1][0] == "0"
                and runs[i + 1][0] == "0"
            ):
                gain = runs[i - 1][1] + runs[i + 1][1]
                max_gain = max(max_gain, gain)

        return active + max_gain