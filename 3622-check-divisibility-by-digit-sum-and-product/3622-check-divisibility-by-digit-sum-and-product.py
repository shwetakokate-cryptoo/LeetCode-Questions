class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1

        x = n

        while x:
            x, digit = divmod(x, 10)
            s += digit 
            p *= digit

        return n % (s + p ) == 0