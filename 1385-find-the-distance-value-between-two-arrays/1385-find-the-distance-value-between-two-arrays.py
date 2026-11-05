class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0

        for x in arr1:
            valid = True

            for y in arr2:
                if abs(x - y) <= d:
                    valid = False
                    break

            if valid:
                count += 1

        return count