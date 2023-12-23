class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        for idx in range(len(nums) - 2, 0, -1):
            if nums[idx] == 0:
                temp = 2
                for idx2 in range(idx - 1, -1, -1):
                    if nums[idx2] < temp:
                        temp += 1
                    else:
                        temp = 0
                        break
                if temp != 0:
                    return False
        return True


nums = [2,0,0]
print(Solution().canJump(nums))
