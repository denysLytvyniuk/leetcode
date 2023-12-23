class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        ranges = [[nums[0], 0]]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1:
                ranges.append([nums[i], 0])
            else:
                ranges[len(ranges)-1][1] = nums[i]
        for idx in range(len(ranges)):
            if ranges[idx][1] == 0:
                ranges[idx] = str(ranges[idx][0])
            else:
                ranges[idx] = str(ranges[idx][0]) + '->' + str(ranges[idx][1])
        return ranges


print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))