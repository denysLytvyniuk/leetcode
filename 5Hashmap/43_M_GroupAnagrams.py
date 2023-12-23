class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        res = {}

        for s in strs:
            canonical = "".join(sorted(s))
            if canonical in res:
                res[canonical].append(s)
            else:
                res[canonical] = [s]

        return res.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(strs = ["a"]))