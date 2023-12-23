class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numbers = sorted(nums)
        l, r = 0, len(numbers)-1
        while True:
            summ = numbers[l] + numbers[r]
            if summ == target:
                if numbers[l] == numbers[r]:
                    idxl = nums.index(numbers[l])
                    nums[idxl] += 1
                    return [idxl, nums.index(numbers[r])]
                else:
                    return [nums.index(numbers[l]) , nums.index(numbers[r])]
            elif summ < target:
                l += 1
            else:
                r -= 1


print(Solution().twoSum(nums = [2,7,11,15], target = 9))
print(Solution().twoSum(nums = [3,2,4], target = 6))
print(Solution().twoSum(nums = [3,3], target = 6))