class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers)-1
        while True:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l+1, r+1]
            elif summ < target:
                l += 1
            else:
                r -= 1


print(Solution().twoSum([2,7,11,15], 9))