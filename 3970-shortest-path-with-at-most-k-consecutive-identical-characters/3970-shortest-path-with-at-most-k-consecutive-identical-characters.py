
import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):
        mavorqeli = (n, edges, labels, k)

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [[float('inf')] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]
        dist[0][1] = 0

        while pq:
            cost, node, count = heapq.heappop(pq)

            if cost != dist[node][count]:
                continue

            if node == n - 1:
                return cost

            for nei, weight in graph[node]:
                if labels[nei] == labels[node]:
                    new_count = count + 1
                else:
                    new_count = 1

                if new_count > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[nei][new_count]:
                    dist[nei][new_count] = new_cost
                    heapq.heappush(pq, (new_cost, nei, new_count))

        return -1

