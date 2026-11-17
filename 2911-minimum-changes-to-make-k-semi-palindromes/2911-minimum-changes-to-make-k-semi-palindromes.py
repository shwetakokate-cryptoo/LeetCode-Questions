
class Solution:
    def minimumChanges(self, s, k):
        n = len(s)
        INF = float('inf')

        cost = [[INF] * (n + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    for p in range(length):
                        q = ((length // d - 1 - p // d) * d
                             + p % d)

                        if p >= q:
                            break

                        if s[i + p] != s[i + q]:
                            changes += 1

                    cost[i][j + 1] = min(
                        cost[i][j + 1], changes
                    )

        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for parts in range(1, k + 1):
                for j in range(i - 1):
                    dp[i][parts] = min(
                        dp[i][parts],
                        dp[j][parts - 1] + cost[j][i]
                    )

        return dp[n][k]
