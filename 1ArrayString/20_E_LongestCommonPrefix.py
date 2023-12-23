class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for i in range(min([len(l) for l in strs])):
            res += strs[0][i]
            for s in strs[1:]:
                if s[i] != res[i]:
                    return res[:-1]
        return res
print(Solution().longestCommonPrefix(["dog","racecar","car"]))