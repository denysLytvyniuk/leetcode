class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []
        for val in tokens:
            if val.isnumeric():
                stack.append(int(val))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if val == '/':
                    stack.append(int(float(num2)/num1))
                elif val == '-':
                    stack.append(num2 - num1)
                elif val == '*':
                    stack.append(num2 * num1)
                else:
                    stack.append(num2 + num1)

        return stack.pop()


print(Solution().evalRPN(["2","1","+","3","*"]))
print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))