class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ((3 * sum(set(nums))) - sum(nums)) // 2


print(Solution().singleNumber([2, 2, 3, 2]))
print(Solution().singleNumber([0, 1, 0, 1, 0, 1, 99]))
