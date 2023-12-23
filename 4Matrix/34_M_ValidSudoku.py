class Solution(object):
    def check(self, arr):
        for num in arr:
            if num != '.' and arr.count(num) > 1:
                return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cubes = [[] for _ in range(9)]
        for idx, line in enumerate(board):
            for i in range(9):
                cubes[idx // 3 * 3 + i // 3].append(line[i])
        for i in range(len(board)):
            if not self.check(board[i]) or not self.check([subarray[i] for subarray in board]) or not self.check(cubes[i]):
                return False

        return True



print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                   , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                   , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                   , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                   , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                   , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                   , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                   , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                   , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
print(Solution().isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                   , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                   , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                   , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                   , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                   , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                   , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                   , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                   , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
