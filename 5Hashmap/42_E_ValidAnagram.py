class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(list(s)) == sorted(list(t))


print(Solution().isAnagram(s = "anagram", t = "nagaram"))
print(Solution().isAnagram(s = "rat", t = "car"))