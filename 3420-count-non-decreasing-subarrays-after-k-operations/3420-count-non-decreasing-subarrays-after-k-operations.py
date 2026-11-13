
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        n = len(nums)
        dq = deque()
        cost = 0
        ans = 0
        j = n - 1

        for i in range(n - 1, -1, -1):
            while dq and nums[dq[-1]] < nums[i]:
                left = dq.pop()
                right = dq[-1] if dq else j + 1
                cost += (right - left) * (nums[i] - nums[left])

            dq.append(i)

            while cost > k:
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            ans += j - i + 1

        return ans
