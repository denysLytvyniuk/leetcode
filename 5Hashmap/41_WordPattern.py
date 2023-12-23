class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        if len(s.split(' ')) != len(pattern):
            return False
        d = {}

        for idx, c in enumerate(s.split(' ')):
            if d.__contains__(c):
                if pattern[idx] != d.get(c):
                    return False
            else:
                if pattern[idx] in d.values():
                    return False
                d[c] = pattern[idx]

        return True

print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dog"))
print(Solution().wordPattern(pattern = "abba", s = "dog cat cat asd"))