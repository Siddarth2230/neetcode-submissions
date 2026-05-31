class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestStock = prices[0]

        for price in prices:
            if price > lowestStock:
                maxProfit = max(maxProfit, price - lowestStock)
            
            lowestStock = min(lowestStock, price)
        
        return maxProfit


