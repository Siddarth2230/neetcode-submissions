class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        maxCount = 1
        for key in mp.keys():
            if (key-1) in mp:
                continue
            count = 1
            while (key+1) in mp:
                count += 1
                maxCount = max(count, maxCount)
                key += 1
        
        return maxCount