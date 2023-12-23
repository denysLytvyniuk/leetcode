class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        while n not in d:
            d.add(n)
            n = sum([int(s) ** 2 for s in str(n)])
            if n == 1:
                return True
        return False


print(Solution().isHappy(19))
print(Solution().isHappy(2))
