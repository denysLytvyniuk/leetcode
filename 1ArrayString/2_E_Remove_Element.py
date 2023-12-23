class Solution(object):
    def removeElement(self, nums: list[int], val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        for idx, item in enumerate(nums):
            if item == val:
                nums[idx] = max(nums) + 1
                k -= 1
        nums.sort()
        nums = nums[:k]
        return k


arr = [1, 2, 0]
print(arr)
print(Solution().removeElement(arr, 2))
print(arr)