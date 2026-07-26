class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = [[] for _ in range(n+1)]
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        for key, value in mp.items():
            freq[value].append(key)
        
        res = []
        for i in range(n, -1, -1):
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
