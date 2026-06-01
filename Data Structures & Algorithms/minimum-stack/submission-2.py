class MinStack:

    def __init__(self):
        self.st = []
        
    def push(self, val: int) -> None:
        st = self.st
        if not st:
            st.append((val, val))
        else:
            st.append((val,min(val, st[-1][1])))

    def pop(self) -> None:
        st = self.st
        st.pop()

    def top(self) -> int:
        st = self.st
        return st[-1][0]

    def getMin(self) -> int:
        st = self.st
        return st[-1][1]
        
        

