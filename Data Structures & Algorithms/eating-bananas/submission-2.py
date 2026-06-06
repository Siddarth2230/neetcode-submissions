class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canFinish(speed):
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed
        
            return hours <= h

        while l < r:
            m = l + (r-l)//2

            if canFinish(m):
                r = m
            else:
                l = m+1
        
        return r

