class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        hash = [0] * (n+1)

        for num in nums:
            hash[num] += 1

            if hash[num] > 1:
                return num
        
        