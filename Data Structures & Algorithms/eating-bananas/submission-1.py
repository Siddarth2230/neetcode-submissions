class Solution:
    def findMax(self, piles):
        maxEle = float("-inf")

        for pile in piles:
            maxEle = max(maxEle, pile)
        
        return maxEle
    
    def findNumberOfHours(self, piles, count):
        countHours = 0

        for pile in piles:
            countHours += (pile + count - 1) // count
        
        return countHours
        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, self.findMax(piles)

        while l < r:
            m = l + (r-l)//2

            hours = self.findNumberOfHours(piles, m)
            print(f"{m},{hours}")

            if hours <= h:
                r = m
            else:
                l = m+1
        
        return r

