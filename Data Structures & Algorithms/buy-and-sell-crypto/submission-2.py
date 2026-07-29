class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] > minPrice:
                maxProfit = max(prices[i] - minPrice, maxProfit)
            elif prices[i] < minPrice:
                minPrice = prices[i]
        
        return maxProfit
            