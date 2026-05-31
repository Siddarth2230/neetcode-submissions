class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = defaultdict(int)
        l, r = 0, 0
        maxLength = 0

        while r < len(s):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
                mp[s[r]] = r
            
            maxLength = max(maxLength, r-l+1)
            mp[s[r]] = r
            r += 1
        
        return maxLength
