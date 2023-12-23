class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])


print(Solution().lengthOfLastWord("   fly me   to   the moon  "))