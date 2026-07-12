class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}

        for i in range(len(nums)):
            if nums[i] not in freq_map:
                freq_map[nums[i]] = 1
            else:
                freq_map[nums[i]] += 1
        
        freq_list = [[] for i in range(len(nums) + 1)]

        for key, value in freq_map.items():
            freq_list[value].append(key)
        
        print(freq_list)

        result = []

        for element in reversed(freq_list):
            for i in element:
                if (len(result) < k):
                    result.append(i)

        return result

