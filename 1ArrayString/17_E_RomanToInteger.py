class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        result = 0
        for i in range(len(s)-1):
                if arr[s[i]] < arr[s[i+1]]:
                    result -= arr.get(s[i])
                else:
                    result += arr.get(s[i])
        return result + arr[s[-1]]


print(Solution().romanToInt("LVIII"))
