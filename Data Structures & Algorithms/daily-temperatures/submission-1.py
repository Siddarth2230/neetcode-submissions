class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []
        
        for i, temp in enumerate(temperatures):
            
            while st and temp > temperatures[st[-1]]:
                index = st.pop()
                res[index] = i - index

            st.append(i)
        
        return res
            
            
