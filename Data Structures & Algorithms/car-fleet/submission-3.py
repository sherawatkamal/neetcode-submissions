class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        indices = sorted(range(len(position)), key=lambda i: position[i], reverse=True)

        sorted_position = [position[i] for i in indices]
        sorted_speed    = [speed[i] for i in indices]
        
        time_list = []

        for i in range(len(position)):
            time = (target - sorted_position[i])/sorted_speed[i]

            if i == 0:
                time_list.append(time)
            else:
                if time < time_list[i-1]:
                    time = time_list[i-1]
                    time_list.append(time)
                else:
                    time_list.append(time)
        
        time_set = set(time_list)

        return len(time_set)
            