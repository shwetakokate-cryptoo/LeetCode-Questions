class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                parent[b] = a

        for a, b in allowedSwaps:
            union(a, b)

        groups = {}

        for i in range(n):
            root = find(i)
            groups.setdefault(root, {})
            groups[root][source[i]] = groups[root].get(source[i], 0) + 1

        ans = 0

        for i in range(n):
            root = find(i)
            value = target[i]

            if groups[root].get(value, 0) > 0:
                groups[root][value] -= 1
            else:
                ans += 1

        return ans