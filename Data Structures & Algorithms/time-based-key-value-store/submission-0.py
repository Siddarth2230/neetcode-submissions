class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.mp[key]
        value = ""
        if not values:
            return value

        l, r = 0, len(values)-1

        while l <= r:
            m = l + (r-l)//2
            time = values[m][1]

            if time <= timestamp:
                value = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return value
        
        

        
        
