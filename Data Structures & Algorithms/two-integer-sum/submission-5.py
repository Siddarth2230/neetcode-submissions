class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # second number = target - nums[i]
        mp = defaultdict(int)

        for i,num in enumerate(nums):
            rem = target - num

            if rem in mp:
                return [mp[rem], i]
            
            mp[num] = i

        
        