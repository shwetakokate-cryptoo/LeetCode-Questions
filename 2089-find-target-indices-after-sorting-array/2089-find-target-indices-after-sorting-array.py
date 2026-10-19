
class Solution:
    def targetIndices(self, nums, target):
        nums.sort()
        return [i for i, num in enumerate(nums) if num == target]
