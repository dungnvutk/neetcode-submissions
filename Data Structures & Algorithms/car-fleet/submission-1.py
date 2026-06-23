class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Get the number of cars
        n = len(position)

        # 2. Sort the indices [0, 1, ..., n-1] based on their starting position in descending order
        sorted_indices = sorted(range(n), key=lambda i: position[i], reverse=True)

        fleets = 0
        current_max_time = 0.0

        # 3. Process each car from closest to furthest from the target
        for i in sorted_indices:
            # Calculate time to target for the current car using its index
            car_time = (target - position[i]) / speed[i]
            
            # If this car takes more time than the fleet in front, it starts a new fleet
            if car_time > current_max_time:
                fleets += 1
                current_max_time = car_time  # This car is now the bottleneck for cars behind it

        return fleets