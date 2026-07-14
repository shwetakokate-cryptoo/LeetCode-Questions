class Solution:
    def subsequencePairCount(self, nums):
        MOD = 1000000007

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        dp = {(0, 0): 1}

        for x in nums:
            new_dp = dp.copy()

            for (g1, g2), count in dp.items():
                ng1 = gcd(g1, x)
                ng2 = gcd(g2, x)

                new_dp[(ng1, g2)] = (new_dp.get((ng1, g2), 0) + count) % MOD
                new_dp[(g1, ng2)] = (new_dp.get((g1, ng2), 0) + count) % MOD

            dp = new_dp

        answer = 0

        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 != 0:
                answer = (answer + count) % MOD

        return answer