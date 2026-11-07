
import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        result = []

        time = 0

        for i, duration in enumerate(tasks):
            time = max(time, i)

            while busy and busy[0][0] <= time:
                end_time, weight, server = heapq.heappop(busy)
                heapq.heappush(available, (weight, server))

            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end_time, weight, server = heapq.heappop(busy)
                    heapq.heappush(available, (weight, server))

            weight, server = heapq.heappop(available)
            result.append(server)

            heapq.heappush(
                busy,
                (time + duration, weight, server)
            )

        return result
