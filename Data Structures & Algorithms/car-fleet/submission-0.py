class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        fleets = 0
        slowest_car = 0

        for start, speed in cars:
            current_car = (target - start) / speed
            if slowest_car < current_car:
                fleets += 1
                slowest_car = current_car
        
        return fleets
        