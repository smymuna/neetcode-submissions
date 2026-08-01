class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        lastTime = 0

        for pos, speed in cars:
            time = (target - pos) / speed

            if time > lastTime:
                fleets += 1
                lastTime = time
        return fleets