class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {
            '{':'}',
            '[':']',
            '(':')',
        }
        if s[0] not in d or len(s) % 2 == 1:
            return False
        stack = []
        for char in s:
            if char in d:
                stack.append(char)
            elif char in d.values():
                if d[stack[len(stack)-1]] == char:
                    stack.pop(len(stack)-1)
                else:
                    return False
        if stack:
            return False
        return True


print(Solution().isValid("()"))
print(Solution().isValid("()[]{}"))
print(Solution().isValid("(]"))