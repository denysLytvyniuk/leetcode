class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 2 or numRows == 1:
            return s
        res = ''
        for i in range(numRows):
            idx = i
            if i == 0 or i == numRows-1:
                while idx < len(s):
                    res += s[idx]
                    idx += numRows + numRows - 2
            else:
                while idx < len(s):
                    res += s[idx]
                    if (idx - i) % (numRows + numRows - 2) == 0:
                        idx += (numRows - i - 1) * 2
                    else:
                        idx += i * 2
        return res


print(Solution().convert("PAYPALISHIRING", 2))
print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("A", 1))