class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        for c in s:
            f = t.find(c)
            if f!= -1:
                t = t[f+1:]
            else:
                return False
        return True


print(Solution().isSubsequence("abc","ahbgd"))