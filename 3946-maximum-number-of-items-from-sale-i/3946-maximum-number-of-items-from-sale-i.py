
class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)
        free = [0] * n
        cheapest = float('inf')

        valmorendi = items

        for i in range(n):
            f, p = items[i]
            cheapest = min(cheapest, p)

            for j in range(n):
                if i != j and items[j][0] % f == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            price = items[i][1]
            value = free[i] + 1

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + value)

        ans = 0

        for j in range(budget + 1):
            ans = max(ans, dp[j] + (budget - j) // cheapest)

        return ans
