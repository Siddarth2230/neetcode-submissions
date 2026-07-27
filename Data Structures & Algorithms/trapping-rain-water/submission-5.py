class Solution:
    def trap(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        maxLeft, maxRight = nums[l], nums[r]
        maxWater = 0
        while l < r:

            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, nums[l])
                if maxLeft > nums[l]:
                    maxWater += (maxLeft - nums[l])
            else:
                r -= 1
                maxRight = max(nums[r], maxRight)
                if maxRight > nums[r]:
                    maxWater += (maxRight - nums[r])
        
        return maxWater
