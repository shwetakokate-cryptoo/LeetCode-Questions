class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
        comp = [0] * n
        cid = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid
        
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])
        
        return ans