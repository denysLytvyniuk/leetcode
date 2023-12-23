class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        temp = matrix[:]
        for i in range(m):
            line = matrix[i]
            if line.__contains__(0) and line.count(0) < n:
                matrix[i] = [0]*n

        for j in range(n):
            row = [sub[j] for sub in temp]
            if row.__contains__(0) and row.count(0) < m:
                for k in range(m):
                    matrix[k][j] = 0


m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(m1)
Solution().setZeroes(m1)
print(m1)

m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
print(m2)
Solution().setZeroes(m2)
print(m2)
