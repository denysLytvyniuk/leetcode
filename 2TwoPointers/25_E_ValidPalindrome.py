import re


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        for st in s:
            if not st.isalpha() and not st.isnumeric():
                s = s.replace(st, '')
        return s == s[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("A man, a plan, a canal: Pnama"))