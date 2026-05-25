class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i in range(len(s)):
            st = set()
            while i < len(s) and s[i] not in st:
                st.add(s[i])
                i += 1
                maxLength = max(len(st),maxLength)
        
        return maxLength
            
                


        