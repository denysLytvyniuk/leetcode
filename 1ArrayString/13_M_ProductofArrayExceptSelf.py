class Solution:
  def productExceptSelf(self, nums):
    n = len(nums)
    result = [1] * n
    # calculate the product of elements to the left of each element and store in result
    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    # calculate the product of elements to the right of each element and update result
    right_product = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]

    return result


nums1 = [-1, 1, 0, -3, 3]
print(Solution().productExceptSelf(nums1))
