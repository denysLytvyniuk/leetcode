class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0  # declaring a left variable starting at 0
        ans = len(nums) + 1  # setting a defult value of ans
        s = 0  # initial sum of the subarrays
        for r in range(len(nums)):  # iterating the right till last
            s += nums[r]  # will add the right element to the sum
            if s >= target:  # add to answer if target is fulfilled
                ans = min(ans, r - l + 1)  # minimum of answer is taken
            while s > target:  # we will shift the right till target not satisfied
                s -= nums[l]
                l += 1
                if s >= target:
                    ans = min(ans, r - l + 1)  # will add the target fulfilled
        return ans if ans < len(nums) + 1 else 0


print(Solution().minSubArrayLen(7, [1, 1, 1, 1, 7]))
print(Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))
print(Solution().minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
print(Solution().minSubArrayLen(11, [1, 2, 3, 4, 5]))
