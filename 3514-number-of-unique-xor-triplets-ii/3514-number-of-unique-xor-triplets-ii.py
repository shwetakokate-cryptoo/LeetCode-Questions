from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX_XOR = 2048

        # Presence array.
        a = [0] * MAX_XOR
        for x in nums:
            a[x] = 1

        # Fast Walsh-Hadamard Transform for XOR convolution.
        def fwht(arr, inverse=False):
            n = len(arr)
            length = 1

            while length < n:
                step = length * 2
                for i in range(0, n, step):
                    for j in range(length):
                        x = arr[i + j]
                        y = arr[i + j + length]

                        arr[i + j] = x + y
                        arr[i + j + length] = x - y

                length <<= 1

            if inverse:
                for i in range(n):
                    arr[i] //= n

        # Transform.
        fwht(a)

        # Cube every coefficient.
        for i in range(MAX_XOR):
            a[i] = a[i] * a[i] * a[i]

        # Inverse transform.
        fwht(a, True)

        # Count achievable XOR values.
        answer = 0
        for x in a:
            if x != 0:
                answer += 1

        return answer