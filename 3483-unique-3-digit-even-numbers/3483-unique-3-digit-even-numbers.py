class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i != j and i != k and j != k:
                        if digits[i] != 0 and digits[k] % 2 == 0:
                            nums.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return len(nums)