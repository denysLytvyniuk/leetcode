class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_left = prices[0]
        for idx, price in enumerate(prices):
            if price < min_left:
                min_left = price
            elif price > min_left:
                if price-min_left > profit:
                    profit = price - min_left
        return profit


arr = [7, 1, 5, 3, 6, 4]
print(Solution().maxProfit(arr))
