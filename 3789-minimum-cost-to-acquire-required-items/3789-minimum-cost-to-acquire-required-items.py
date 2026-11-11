
class Solution:
    def minimumCost(self, cost1, cost2, costBoth, need1, need2):
        a = need1 * cost1 + need2 * cost2

        b = max(need1, need2) * costBoth

        mn = min(need1, need2)
        c = (mn * costBoth +
             (need1 - mn) * cost1 +
             (need2 - mn) * cost2)

        return min(a, b, c)
