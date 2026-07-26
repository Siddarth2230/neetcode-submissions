class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            l, r = i+1, n-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while r > l and nums[r] == nums[r+1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans
                    