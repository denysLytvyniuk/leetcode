class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        for idx in range(len(nums)-1):
            if nums[idx + 1:idx+1+k].__contains__(nums[idx]):
                return True
        return False


print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
print(Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))
