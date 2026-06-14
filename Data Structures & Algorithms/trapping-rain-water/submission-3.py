class Solution:
    def trap(self, nums: List[int]) -> int:
        if not nums: return 0
        maxWater = 0;
        l, r = 0, len(nums)-1
        maxLeft, maxRight = nums[l], nums[r]

        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, nums[l])
                maxWater += (maxLeft - nums[l]) # gives amount of water we can store at that index
            else:
                r -= 1
                maxRight = max(maxRight, nums[r])
                maxWater += (maxRight - nums[r])
            
        return maxWater
        