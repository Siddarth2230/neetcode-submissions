class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = [0] * 256

        for ch in t:
            hash[ord(ch)] += 1

        l, r = 0, 0
        startIndex = -1
        minLength = float("inf")
        count = 0

        while r < len(s):
            if hash[ord(s[r])] > 0:
                count += 1
            
            hash[ord(s[r])] -= 1

            while count == len(t):
                if (r-l+1) < minLength:
                    minLength = r-l+1
                    startIndex = l
                
                hash[ord(s[l])] += 1

                if hash[ord(s[l])] > 0:
                    count -= 1
                
                l += 1
            
            r += 1
        
        return "" if startIndex == -1 else s[startIndex : startIndex+minLength]
            
                


            
                
