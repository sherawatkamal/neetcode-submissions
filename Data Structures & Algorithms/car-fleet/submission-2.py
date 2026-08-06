class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        indices = sorted(range(len(position)), key=lambda i: position[i], reverse=True)

        sorted_position = [position[i] for i in indices]
        sorted_speed    = [speed[i] for i in indices]
        
        fleets = 0
        prev_time = 0.0

        for i in range(len(position)):
            time = (target - sorted_position[i]) / sorted_speed[i]
            if time > prev_time:
                fleets += 1
                prev_time = time
            # else: this car merges into the fleet ahead; prev_time unchanged

        return fleets