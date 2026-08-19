from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = defaultdict(int)

        for row, seat in reservedSeats:
            rows[row] |= 1 << (10 - seat)

        masks = (
            0b0111100000,
            0b0001111000,
            0b0000011110
        )

        ans = (n - len(rows)) * 2

        for seats in rows.values():
            for mask in masks:
                if seats & mask == 0:
                    seats |= mask
                    ans += 1

        return ans