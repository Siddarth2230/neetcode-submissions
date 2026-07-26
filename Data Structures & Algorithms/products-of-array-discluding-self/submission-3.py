class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left, right = 1, 1
        for i in range(0,n):
            ans[i] *= left
            ans[n-i-1] *= right
            
            left, right = left * nums[i], right * nums[n-i-1]
        
        return ans