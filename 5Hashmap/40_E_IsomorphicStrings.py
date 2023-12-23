class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars = {}
        for idx, c in enumerate(s):
            if chars.__contains__(c):
                if t[idx] != chars.get(c):
                    return False
            else:
                if t[idx] in chars.values() :
                    return False
                chars[c] = t[idx]

        return True


print(Solution().isIsomorphic("badc", "baba"))

