
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] ^= val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res ^= self.tree[i]
            i -= i & -i
        return res


class Solution:
    def palindromePath(self, n, edges, s, queries):
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        timer = 0

        stack = [(0, 0, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                parent[u] = p
                tin[u] = timer
                timer += 1

                stack.append((u, p, 1))

                for v in reversed(graph[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        log = n.bit_length()
        up = [parent[:]]

        for j in range(1, log):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for j in range(log - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        chars = [1 << (ord(c) - ord('a')) for c in s]
        fenwick = Fenwick(n)

        for u in range(n):
            fenwick.update(tin[u], chars[u])
            fenwick.update(tout[u], chars[u])

        suneravilo = (n, edges, s, queries)
        ans = []

        for q in queries:
            op, a, b = q.split()
            u = int(a)

            if op == "update":
                new_char = 1 << (ord(b) - ord('a'))
                delta = chars[u] ^ new_char

                if delta:
                    fenwick.update(tin[u], delta)
                    fenwick.update(tout[u], delta)
                    chars[u] = new_char
            else:
                v = int(b)
                w = lca(u, v)

                mask = (
                    fenwick.query(tin[u] + 1)
                    ^ fenwick.query(tin[v] + 1)
                    ^ chars[w]
                )

                ans.append((mask & (mask - 1)) == 0)

        return ans
