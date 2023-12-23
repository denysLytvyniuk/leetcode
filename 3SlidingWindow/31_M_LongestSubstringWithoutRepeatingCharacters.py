class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        res = 0
        l = 0
        for i in range(len(s)):
            if s[i] not in d:
                res = max(res, i-l+1)
            else:
                if d[s[i]] < l:
                    res = max(res,i-l+1)
                else:
                    l = d[s[i]] + 1
            d[s[i]] = i
        return res


print(Solution().lengthOfLongestSubstring("abcdabcbb"))