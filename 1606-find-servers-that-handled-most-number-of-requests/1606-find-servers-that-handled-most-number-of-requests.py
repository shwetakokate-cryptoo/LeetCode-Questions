
import heapq

class Solution:
    def busiestServers(self, k, arrival, load):
        available = list(range(k))
        heapq.heapify(available)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            start = arrival[i]

            while busy and busy[0][0] <= start:
                end, server = heapq.heappop(busy)
                idx = i + (server - i) % k
                heapq.heappush(available, idx)

            if not available:
                continue

            server = heapq.heappop(available) % k

            count[server] += 1
            heapq.heappush(
                busy,
                (start + load[i], server)
            )

        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
