class Solution(object):
    def rotate(self, nums: list, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


arr = [1, 2, 3, 4, 5, 6, 7]
print(Solution().rotate(arr, 8))
print(arr)