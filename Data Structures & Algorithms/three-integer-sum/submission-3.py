class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = set()

        for i in range(n):
            seen = {}

            for j in range(i+1, n):
                rem = -(nums[i] + nums[j])

                if rem in seen:
                    triplet = tuple(sorted((nums[i], nums[j], rem)))
                    s.add(triplet)
                
                seen[nums[j]] = j
        
        return list(s)
                    