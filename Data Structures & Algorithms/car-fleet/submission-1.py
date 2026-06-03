class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed),reverse=True)
        
        fleets = 0
        prevTime = 0

        for p, s in pair:
            currTime = (target - p) / s

            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        
        return fleets


        
        