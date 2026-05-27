class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                return True
            mp[nums[i]] = mp.get(nums[i],0) + 1;
        return False
        