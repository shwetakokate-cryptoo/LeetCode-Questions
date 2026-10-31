
class Solution:
    def uniquePaths(self, grid):
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7

        dp = [[[0, 0] for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 1

        for i in range(m):
            for j in range(n):
                for d in range(2):
                    ways = dp[i][j][d]

                    if ways == 0:
                        continue

                    if grid[i][j] == 0:
                        if j + 1 < n:
                            dp[i][j + 1][0] = (dp[i][j + 1][0] + ways) % mod

                        if i + 1 < m:
                            dp[i + 1][j][1] = (dp[i + 1][j][1] + ways) % mod

                    else:
                        if d == 0 and i + 1 < m:
                            dp[i + 1][j][1] = (dp[i + 1][j][1] + ways) % mod

                        elif d == 1 and j + 1 < n:
                            dp[i][j + 1][0] = (dp[i][j + 1][0] + ways) % mod

        return sum(dp[m - 1][n - 1]) % mod
