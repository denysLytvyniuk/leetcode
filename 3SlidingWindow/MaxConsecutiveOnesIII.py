class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if nums.count(0) == k:
            return n
        res = k
        temp = k
        temps = []
        left = 0
        i = 0
        while i < n:
            if not nums[i]:
                if temp:
                    temps.append(i)
                    temp -= 1
                else:
                    res = max(res, i-left)
                    temps.append(i)
                    if temps:
                        temps.pop(0)
                        left = temps[0]
                    else:
                        left = i
            i += 1
        return res


print(Solution().longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))