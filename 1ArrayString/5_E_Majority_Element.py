class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set(nums)
        for n in my_set:
            if nums.count(n) > len(nums)/2:
                return n


arr = [1, 2, 3, 3, 3, 3, 4]
print(set(arr))
print(Solution().majorityElement(arr))