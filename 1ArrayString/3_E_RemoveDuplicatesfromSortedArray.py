class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for item in nums:
            count = nums.count(item)
            for i in range(count - 1):
                nums.remove(item)
        return len(nums)

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1


arr = [1, 2, 2, 3, 3, 3, 4]
print(arr)
print(Solution().removeDuplicates(arr))
print(arr)