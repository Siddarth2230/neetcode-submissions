class Solution:
    def findZeroCount(self, nums):
        count = 0
        for num in nums: # O(N)
            if num == 0:
                count += 1
        
        return count

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = self.findZeroCount(nums)
        res = []

        if zeroes > 1:
            res = [0] * len(nums)
            return res
        
        product = 1;

        for num in nums: # O(N)
            if num != 0:
                product *= num

        res = [product] * len(nums)

        i=0
        for i in range(len(nums)): # O(N)
            if zeroes and nums[i] != 0:
                res[i] = 0
            if not zeroes:
                res[i] //= nums[i]

        return res


        




        
        

        