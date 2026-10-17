
class Solution:
    def minSwaps(self, nums):
        def digit_sum(x):
            return sum(int(d) for d in str(x))

        n = len(nums)
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {num: i for i, num in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
