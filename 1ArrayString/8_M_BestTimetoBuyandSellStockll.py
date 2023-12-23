class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for idx in range(len(prices) - 1, 0, -1):
            if prices[idx] > prices[idx-1]:
                profit += prices[idx] - prices[idx-1]
        return profit


arr = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(arr))
