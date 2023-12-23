class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        m = len(matrix)
        n = len(matrix[0])
        temp = matrix[:]
        while len(res) < m * n:
            if len(temp[0]) == 1:
                for i in range(len(temp)):
                    res.append(temp[i][0])
                return res
            if len(temp) == 1:
                for t in temp[0]:
                    res.append(t)
                break
            for t in temp[0]:
                res.append(t)
            l_t = len(temp)
            l_t_i = len(temp[0])
            if l_t > 2:
                for i in range(1, l_t - 1):
                    res.append(temp[i][l_t_i-1])
            for t in reversed(temp[l_t-1]):
                res.append(t)
            if l_t > 2:
                for i in range(l_t - 2, 0, -1):
                    res.append(temp[i][0])
            temp = temp[1:l_t-1]
            temp = [sub[1:l_t_i-1] for sub in temp]
        return res

print(Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(Solution().spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))