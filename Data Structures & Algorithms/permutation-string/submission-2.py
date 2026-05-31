class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1, freq_s2 = [0] * 26, [0] * 26
        for ch in s1:
            freq_s1[ord(ch) - ord('a')] += 1
        
        l, r = 0, 0
        while r < len(s2):
            freq_s2[ord(s2[r]) - ord('a')] += 1
            if r-l+1 == len(s1):

                if freq_s2 == freq_s1:
                    return True

                freq_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            r += 1
        
        return False