class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        cur = 1
        nums = sorted(list(set(nums)))
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                cur += 1
            else:
                res = max(res, cur)
                cur = 1
        res = max(res, cur)
        return res


print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

