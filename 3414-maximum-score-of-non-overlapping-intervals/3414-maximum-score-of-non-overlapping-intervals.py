class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        arr = sorted((r, l, w, i) for i, (l, r, w) in enumerate(intervals))
        ends = [x[0] for x in arr]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b
            return a if a[1] < b[1] else b

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            r, l, w, idx = arr[i - 1]

            lo, hi = 0, i - 1
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if ends[mid] < l:
                    lo = mid
                else:
                    hi = mid - 1

            p = lo + 1 if i > 1 and ends[lo] < l else 0

            for k in range(1, 5):
                best = dp[i - 1][k]

                prev_score, prev_indices = dp[p][k - 1]
                candidate = (
                    prev_score + w,
                    tuple(sorted(prev_indices + (idx,)))
                )

                dp[i][k] = better(best, candidate)

        ans = (0, ())
        for k in range(1, 5):
            ans = better(ans, dp[n][k])

        return list(ans[1])