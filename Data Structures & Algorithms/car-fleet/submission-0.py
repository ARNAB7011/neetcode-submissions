class Solution:
    def carFleet(self, target, position, speed):
        n = len(position)

        cars = []

        for i in range(n):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))

        # Sort by position
        cars.sort()

        fleets = 0
        lastTime = 0

        # Start from the car closest to target
        for i in range(n - 1, -1, -1):
            currentTime = cars[i][1]

            if currentTime > lastTime:
                fleets += 1
                lastTime = currentTime

        return fleets