class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            stack.append(nei)

                vertices = len(component)
                degree_sum = 0
                for node in component:
                    degree_sum += len(graph[node])

                edge_count = degree_sum // 2

                if edge_count == vertices * (vertices - 1) // 2:
                    ans += 1

        return ans