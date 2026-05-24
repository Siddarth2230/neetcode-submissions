class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        maxRight = prices[len(prices)-1]
        for i in range(len(prices)-1, -1, -1):
            if prices[i] < maxRight:
                maxProfit = max(maxProfit, maxRight - prices[i])
            maxRight = max(prices[i], maxRight)
        
        return maxProfit


        