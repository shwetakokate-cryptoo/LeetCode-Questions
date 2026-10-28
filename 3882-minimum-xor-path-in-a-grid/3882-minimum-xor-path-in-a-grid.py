
class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        limit = 1024

        dp = [[0] * limit for _ in range(n)]
        dp[0][grid[0][0]] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                value = grid[i][j]
                current = [0] * limit

                if i > 0:
                    for x in range(limit):
                        if dp[j][x]:
                            current[x ^ value] = 1

                if j > 0:
                    for x in range(limit):
                        if dp[j - 1][x]:
                            current[x ^ value] = 1

                dp[j] = current

        for x in range(limit):
            if dp[n - 1][x]:
                return x
     