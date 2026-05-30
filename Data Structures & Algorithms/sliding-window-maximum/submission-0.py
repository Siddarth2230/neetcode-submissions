class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for i in range(len(nums)):
            if dq and dq[-1] <= i-k:
                dq.pop()
            
            while(dq and nums[dq[0]] <= nums[i]):
                dq.popleft()
            
            dq.appendleft(i)

            if i >= k-1:
                res.append(nums[dq[-1]])
        
        return res
            




        