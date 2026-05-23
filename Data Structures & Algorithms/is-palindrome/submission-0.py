class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum(): # checks if char is alphabet/digit
                cleaned += ch.lower()
        
        n = len(cleaned)

        for i in range(n // 2):
            if cleaned[i] != cleaned[n-i-1]:
                return False
        
        return True

        