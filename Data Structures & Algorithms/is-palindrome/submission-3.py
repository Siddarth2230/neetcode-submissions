class Solution:
    def isAlphaNumeric(self, ch):
        # 0-9(48-57) A-Z(65-90) a-z(97-122)
        return(
            ord('0') <= ord(ch) <= ord('9') or
            ord('A') <= ord(ch) <= ord('Z') or
            ord('a') <= ord(ch) <= ord('z')
        )

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not self.isAlphaNumeric(s[left]):
                left += 1
            
            while left < right and not self.isAlphaNumeric(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True