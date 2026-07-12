class Solution:
    def arrayRankTransform(self, arr):
        rank = {}

        for x in sorted(arr):
            if x not in rank:
                rank[x] = len(rank) + 1

        return [rank[x] for x in arr]