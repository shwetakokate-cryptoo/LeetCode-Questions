
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        q = sorted((time, i) for i, time in enumerate(queries))
        ans = [0] * len(queries)

        freq = [0] * (n + 1)
        active = 0
        left = right = 0

        for time, idx in q:
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                right += 1

            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans
