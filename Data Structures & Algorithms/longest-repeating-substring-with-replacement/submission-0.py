class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l, r = 0, 0
        maxLength = 0
        maxf = 0

        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, freq[ord(s[r]) - ord('A')])

            if (r-l+1) - maxf > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            maxLength = max(maxLength, r-l+1)
            r += 1
        
        return maxLength