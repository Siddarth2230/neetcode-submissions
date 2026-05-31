class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)-1
        l, r = 0, n
        maxWater = 0

        while l < r:
            water = min(heights[l], heights[r]) * (r-l)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            
            maxWater = max(maxWater, water)
        
        return maxWater
                
        