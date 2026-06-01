class MinStack:

    def __init__(self):
        self.st = []
        self.minValue = float('inf')
        
    def push(self, val: int) -> None:
        if not self.st:
            self.st.append(val)
            self.minValue = val

        elif val >= self.minValue:
            self.st.append(val)

        else:
            self.st.append(2*val - self.minValue)
            self.minValue = val

    def pop(self) -> None:
        if not self.st:
            return
        
        top = self.st.pop()

        if top < self.minValue:
            self.minValue = 2 * self.minValue - top

    def top(self) -> int:
        top = self.st[-1]

        if top < self.minValue:
            return self.minValue
        
        return top

    def getMin(self) -> int:
        return self.minValue
