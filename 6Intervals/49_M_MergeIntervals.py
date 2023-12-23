class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        res = sorted(intervals)
        while i < len(res) - 1:
            if res[i][1] >= res[i+1][0]:
                if res[i][1] < res[i+1][1]:
                    res[i][1] = res[i+1][1]
                res.remove(res[i+1])
            else:
                i += 1

        return res


print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))