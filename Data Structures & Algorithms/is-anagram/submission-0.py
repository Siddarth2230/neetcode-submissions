class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}

        for ch in s:
            mp[ch] = mp.get(ch,0) + 1;
    
        for ch in t:
            mp[ch] = mp.get(ch,0) - 1;

        for value in mp.values():
            if value != 0:
                return False
        
        return True

        
        


        
        