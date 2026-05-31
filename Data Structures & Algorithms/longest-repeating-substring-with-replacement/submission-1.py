class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        n = len(s)
        maxf = 0 # max freq up till there
        l, r = 0, 0
        maxLength = 0 

        while r < n:
            freq[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, freq[ord(s[r]) - ord('A')])

            if ((r-l+1) - maxf) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            maxLength = max(maxLength, r-l+1)
            r += 1
        
        return maxLength




        