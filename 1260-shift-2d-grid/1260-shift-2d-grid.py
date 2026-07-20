from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        nums = []
        for row in  grid:
            nums.extend(row)

        total = rows * cols

        k %= total

        nums = nums[-k:] + nums[:-k]

        answer = []
        index = 0

        for i in range(rows):
            answer.append(nums[index:index + cols])
            index += cols


        return answer