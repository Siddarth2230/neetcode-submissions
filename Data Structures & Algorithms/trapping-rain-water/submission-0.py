class Solution:
    def trap(self, nums: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(nums)-1
        maxLeft = nums[l]
        maxRight = nums[r]

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                water = maxLeft - nums[l]
                if water > 0:
                    maxWater += water
            else:
                r -= 1
                water = maxRight - nums[r]
                if water > 0:
                    maxWater += water
            
            maxLeft = max(maxLeft, nums[l])
            maxRight = max(maxRight, nums[r])
        
        return maxWater
            
            

        
            


        