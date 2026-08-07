class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        need = [0, 0, 0, 0]

        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                need[i] += 1
                t //= p

        if t != 1:
            return "-1"

        f = (
            (0, 0, 0, 0),
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (2, 0, 0, 0),
            (0, 0, 1, 0),
            (1, 1, 0, 0),
            (0, 0, 0, 1),
            (3, 0, 0, 0),
            (0, 2, 0, 0)
        )

        dp = [[99] * 30 for _ in range(47)]
        dp[0][0] = 0

        for a in range(47):
            for b in range(30):
                if dp[a][b] == 99:
                    continue
                for d in range(2, 10):
                    x = min(46, a + f[d][0])
                    y = min(29, b + f[d][1])
                    dp[x][y] = min(dp[x][y], dp[a][b] + 1)

        def min_digits(a, b, c, d):
            return dp[a][b] + c + d

        total_min = min_digits(*need)

        if total_min > len(num):
            return self.build(need, total_min, f, min_digits)

        n = len(num)
        pref = [[0, 0, 0, 0] for _ in range(n + 1)]

        for i, ch in enumerate(num):
            x = f[ord(ch) - 48]
            for j in range(4):
                pref[i + 1][j] = min(need[j], pref[i][j] + x[j])

        if '0' not in num and pref[n] == need:
            return num

        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = n

        for i in range(n - 1, -1, -1):
            if i > first_zero:
                continue

            used = pref[i]
            cur = ord(num[i]) - 48

            for d in range(cur + 1, 10):
                x = f[d]

                rem = [
                    max(0, need[j] - used[j] - x[j])
                    for j in range(4)
                ]

                slots = n - i - 1

                if min_digits(*rem) <= slots:
                    return (
                        num[:i]
                        + str(d)
                        + self.build(rem, slots, f, min_digits)
                    )

        return self.build(need, n + 1, f, min_digits)

    def build(self, need, length, f, min_digits):
        ans = []

        for _ in range(length):
            for d in range(1, 10):
                x = f[d]

                rem = [
                    max(0, need[j] - x[j])
                    for j in range(4)
                ]

                left = length - len(ans) - 1

                if min_digits(*rem) <= left:
                    ans.append(str(d))
                    need = rem
                    break

        return ''.join(ans)