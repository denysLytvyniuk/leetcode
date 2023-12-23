class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) == 1:
            return 1
        arr = sorted(points)
        res = 1
        last = arr[0]
        arr = arr[1:]
        for item in arr:
            if item[0] > last[1]:
                res += 1
                last = item
            elif item[0] == last[1]:
                last[0] = last[1]
            else:
                last[0] = item[0]
                if last[1] > item[1]:
                    last[1] = item[1]
        return res


print(Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
