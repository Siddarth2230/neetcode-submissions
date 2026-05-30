class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums) * 2
        arr = [0] * n

        for i in range(n):
            if i >= len(nums):
                arr[i] = nums[i-n]
            else:
                arr[i] = nums[i]
        
        return arr
        