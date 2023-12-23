class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations = sorted(citations)
        n = len(citations)
        if citations[n-1] == 0: return 0
        for idx, c in enumerate(sorted(citations)):
            if c >= n - idx:
                return n - idx


nums = [0, 0]
print(Solution().hIndex(nums))
