class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for i in range(len(nums) + 1)]
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        for key,val in count.items():
            freq[val].append(key)
        
        ans = []
        for i in range(n,-1,-1):
            for num in freq[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans

            
        