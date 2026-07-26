class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = set(nums)
        maxCount = 0

        for num in mp:
            count = 1
            prevNum = num - 1

            if prevNum in mp:
                continue
            
            nextNum = num + 1
            while nextNum in mp:
                count += 1
                nextNum += 1
            
            maxCount = max(maxCount, count)

        return maxCount