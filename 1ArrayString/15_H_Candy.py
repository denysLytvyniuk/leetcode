class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        result, n = 0, len(ratings)
        candies = [1] * n
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and candies[i] <= candies[i - 1]:
                candies[i] = candies[i-1] + 1
        for j in range(len(ratings)-1, 0, -1):
            if j >= 1 and ratings[j] > ratings[j - 1] and candies[j] <= candies[j - 1]:
                candies[j] = candies[j-1] + 1
            if j < n - 1 and ratings[j] > ratings[j + 1] and candies[j] <= candies[j + 1]:
                candies[j] = candies[j+1] + 1
        return sum(candies)


nums = [1, 2, 87, 87, 87, 2, 1]
nums2 = [5, 4 , 3, 2, 1]

print(Solution().candy(nums))
