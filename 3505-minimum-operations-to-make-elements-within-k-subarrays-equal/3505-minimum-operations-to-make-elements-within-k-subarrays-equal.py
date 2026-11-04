
class Solution:
    def minOperations(self, nums, x, k):
        n = len(nums)
        values = sorted(set(nums))
        m = len(values)

        pos = {v: i + 1 for i, v in enumerate(values)}

        count = [0] * (m + 1)
        total = [0] * (m + 1)

        def update(bit, i, delta):
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s

        def kth(rank):
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step
                if nxt <= m and count[nxt] < rank:
                    idx = nxt
                    rank -= count[nxt]
                step >>= 1

            return idx + 1

        costs = []

        for i in range(n):
            v = nums[i]
            update(count, pos[v], 1)
            update(total, pos[v], v)

            if i >= x:
                old = nums[i - x]
                update(count, pos[old], -1)
                update(total, pos[old], -old)

            if i >= x - 1:
                mid = kth((x + 1) // 2)
                median = values[mid - 1]

                left_count = query(count, mid)
                left_sum = query(total, mid)

                right_count = x - left_count
                right_sum = query(total, m) - left_sum

                cost = (median * left_count - left_sum)
                cost += (right_sum - median * right_count)

                costs.append(cost)

        inf = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [inf] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
