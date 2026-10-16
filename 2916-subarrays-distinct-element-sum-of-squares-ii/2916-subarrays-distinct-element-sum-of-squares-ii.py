
class Solution:
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def push(node, left, right):
            if lazy[node] == 0:
                return

            val = lazy[node]
            length = right - left + 1

            tree_sq[node] = (tree_sq[node] + 2 * val * tree_sum[node] + val * val * length) % MOD
            tree_sum[node] = (tree_sum[node] + val * length) % MOD

            if left != right:
                lazy[node * 2] += val
                lazy[node * 2 + 1] += val

            lazy[node] = 0

        def update(node, left, right, ql, qr):
            push(node, left, right)

            if qr < left or right < ql:
                return

            if ql <= left and right <= qr:
                lazy[node] += 1
                push(node, left, right)
                return

            mid = (left + right) // 2

            update(node * 2, left, mid, ql, qr)
            update(node * 2 + 1, mid + 1, right, ql, qr)

            tree_sum[node] = (tree_sum[node * 2] + tree_sum[node * 2 + 1]) % MOD
            tree_sq[node] = (tree_sq[node * 2] + tree_sq[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)
            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + tree_sq[1]) % MOD
            last[x] = i

        return ans
