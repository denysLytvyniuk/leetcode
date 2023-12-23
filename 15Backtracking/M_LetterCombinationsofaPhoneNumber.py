class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        ans = []
        dial = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def helper(comb, index, digits):
            if index == len(digits):
                ans.append(comb)
                return

            letters = dial[int(digits[index])]
            for char in letters:
                helper(comb + char, index + 1, digits)

        if len(digits) == 0:
            return ans

        helper("", 0, digits)
        return ans

    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # My Solution
        if not digits:
            return []
        reference = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}
        sol = []
        cnt_digits = len(digits)
        for i in range(cnt_digits):
            if not sol:
                sol.extend(reference[digits[i]])
            else:
                tmp = []
                for j in sol:
                    for k in reference[digits[i]]:
                        tmp.append(j + k)
                sol = tmp[:]
        return sol
    