class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]

        l, r = 0, len(values)-1

        while l <= r:
            m = l + (r-l)//2
            time = values[m][1]

            if time <= timestamp:
                l = m + 1
            else:
                r = m - 1
        
        return values[r][0] if r >= 0 else ""
        
        

        
        
