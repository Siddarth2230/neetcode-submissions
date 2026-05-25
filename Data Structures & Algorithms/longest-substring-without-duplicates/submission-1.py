class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        maxLength = 0

        for right in range(len(s)):
            
            while(s[right] in st):
                st.remove(s[left])
                left += 1
            
            st.add(s[right])
            maxLength = max(maxLength, len(st))

        return maxLength
            
                


        