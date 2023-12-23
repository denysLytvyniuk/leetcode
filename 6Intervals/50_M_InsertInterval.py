class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = intervals
        res.append(newInterval)
        res = sorted(res)
        i = res.index(newInterval)
        if i > 0:
            i -= 1
        while i < len(res) - 1:
            if res[i][1] >= res[i + 1][0]:
                if res[i][1] < res[i + 1][1]:
                    res[i][1] = res[i + 1][1]
                res.remove(res[i + 1])
            else:
                i += 1
        return res


print(Solution().insert(intervals = [], newInterval = [2,3]))
print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))