class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = [0] * 256
        
        for ch in t:
            freq[ord(ch)] += 1
        
        count = 0
        startIndex = -1
        l, r = 0, 0
        minLength = float('inf ')

        while r < len(s):

            if freq[ord(s[r])] > 0:
                count += 1
            
            freq[ord(s[r])] -= 1
            
            while count == len(t):
                if r-l+1 < minLength:
                    startIndex = l
                    minLength = r-l+1

                freq[ord(s[l])] += 1

                if freq[ord(s[l])] > 0:
                    count -= 1

                l += 1

            r += 1
        
        return '' if startIndex == -1 else s[startIndex : startIndex + minLength]

                
            

            

            



        