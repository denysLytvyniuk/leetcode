class Solution(object):
    def merge(self, nums1: list, m, nums2, n):
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()



arr = [1, 2, 0]
arr1 = [1]
print(arr)
Solution().merge(arr, 2, arr1, 1)
print(arr)


