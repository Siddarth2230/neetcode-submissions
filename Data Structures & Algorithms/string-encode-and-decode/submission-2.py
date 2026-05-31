class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []

        for word in strs:
            encoded_string.append(str(len(word)) + '&' + word)

        return ''.join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '&':
                j += 1
            
            length = int(s[i:j])
            word = s[j+1:j+length+1]

            decoded.append(word)
            i = j + length + 1
        
        return decoded
            
            

