class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0] * 26
        for ch in s1:
            freq_s1[ord(ch) - ord('a')] += 1
        
        l, r = 0, 0
        while r < len(s2):
            if r-l+1 == len(s1):
                freq = [0] * 26

                for i in range(l,r+1):
                    freq[ord(s2[i]) - ord('a')] += 1
                
                if freq == freq_s1:
                    return True
                l += 1

            r += 1
        
        return False
                



        