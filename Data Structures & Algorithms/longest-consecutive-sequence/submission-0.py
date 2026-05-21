class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set()
        longest = 0

        for num in nums:
            values.add(num)
        
        for value in values:
            prev = value - 1
            next = value + 1
            count = 1

            if prev in values:
                continue
            
            while(next in values):
                count += 1
                next += 1
            
            longest = max(longest, count)
        
        return longest


        
            


        