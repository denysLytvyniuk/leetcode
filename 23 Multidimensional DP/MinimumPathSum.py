from functools import lru_cache
from itertools import product


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        for i, j in product(range(m), range(n)):
            print(str(i) + ' ' + str(j))


nums = [1, 3 , 4]
print(nums.append(2))

