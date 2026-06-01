class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        n = len(s)

        for i in range(n):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                st.append(s[i])
            else:
                if not st:
                    return False
                elif (s[i] == '}' and st[-1] != '{' or
                      s[i] == ')' and st[-1] != '(' or
                      s[i] == ']' and st[-1] != '['):
                      return False
                else:
                    st.pop() 
        
        return True if not st else False

        
        