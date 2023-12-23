class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or nums[0] == 0 or len(nums) == 1:
            return 0
        for idx in range(len(nums)):
            if nums[idx] >= len(nums) - idx - 1:
                return 1 + self.jump(nums[:idx+1])


nums = [1,3,2,2,6]
print(Solution().jump(nums))
