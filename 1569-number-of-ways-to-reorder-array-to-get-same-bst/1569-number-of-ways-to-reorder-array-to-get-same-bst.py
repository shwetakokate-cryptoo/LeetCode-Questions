from math import comb

class Solution:
    def numOfWays(self, nums):
        MOD = 10**9 + 7

        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [x for x in arr[1:] if x < root]
            right = [x for x in arr[1:] if x > root]

            return (comb(len(arr) - 1, len(left)) * dfs(left) * dfs(right)) % MOD

        return (dfs(nums) - 1) % MOD