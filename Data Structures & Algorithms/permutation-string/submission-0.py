class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26

        for ch in s1:
            freq[ord(ch) - ord('a')] += 1

        l, r = 0, 0

        while r < len(s2):
            if r-l+1 == len(s1):
                count = [0] * 26
                for ch in s2[l:r+1]:
                    count[ord(ch) - ord('a')] += 1
                
                if tuple(count) == tuple(freq):
                    return True

                l += 1
    
            r += 1
        
        return False
                
            


        