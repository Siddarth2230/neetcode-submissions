class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        n = len(nums)
        for i in range(n):
            if nums[i] in mp:
                return True
            mp[nums[i]] += 1;
        return False
        