class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        maxCount = 0

        for i,num in enumerate(nums):
            mp[num] = i
        
        for num in mp.keys():
            count = 1
            prevNum = num-1
            if prevNum in mp:
                continue
            
            nextNum = num + 1
            while nextNum in mp:
                count += 1
                nextNum += 1
            
            maxCount = max(maxCount, count)
        
        return maxCount


        