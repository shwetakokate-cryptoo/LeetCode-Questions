class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10 ** 9 + 7
        n = len(s)

        # positions and values of non-zero digits
        pos = []
        val = []
        pref = [0]

        # prefix sum of non-zero digits
        digit_pref = [0] * (n + 1)

        for i, ch in enumerate(s):
            digit_pref[i + 1] = digit_pref[i]
            if ch != '0':
                pos.append(i)
                d = ord(ch) - ord('0')
                val.append(d)
                pref.append(pref[-1] + 1)
                digit_pref[i + 1] += d

        m = len(pos)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # segment tree
        size = 1
        while size < m:
            size <<= 1

        tree = [0] * (2 * size)

        for i in range(m):
            tree[size + i] = val[i]

        for i in range(size - 1, 0, -1):
            left = tree[2 * i]
            right = tree[2 * i + 1]

            # number of digits in right child
            l1 = min(size, max(0, m - ((i * 2 - size) if False else 0)))

            tree[i] = 0

        # Build with lengths
        length = [0] * (2 * size)
        for i in range(size):
            if i < m:
                length[size + i] = 1
        for i in range(size - 1, 0, -1):
            length[i] = length[2 * i] + length[2 * i + 1]
            tree[i] = (tree[2 * i] * pow10[length[2 * i + 1]] + tree[2 * i + 1]) % MOD

        def query(node, nl, nr, l, r):
            if r < nl or nr < l:
                return (0, 0)   # value, length
            if l <= nl and nr <= r:
                return (tree[node], length[node])

            mid = (nl + nr) // 2
            lv, ll = query(node * 2, nl, mid, l, r)
            rv, rl = query(node * 2 + 1, mid + 1, nr, l, r)
            return ((lv * pow10[rl] + rv) % MOD, ll + rl)

        import bisect

        ans = []

        for l, r in queries:
            # sum of non-zero digits
            sm = digit_pref[r + 1] - digit_pref[l]

            # indices of non-zero digits
            L = bisect.bisect_left(pos, l)
            R = bisect.bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            x, _ = query(1, 0, size - 1, L, R)
            ans.append((x * sm) % MOD)

        return ans