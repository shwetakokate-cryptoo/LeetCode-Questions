class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            x = n

            while x > 0:
                product *= x % 10
                x //= 10

            if product % t == 0:
                return n

            n += 1