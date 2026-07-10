class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        my_dict = {num: index for index, num in enumerate(nums)}

        for i in range(len(nums)):
            diff = target - nums[i]
            if (diff in my_dict and my_dict[diff] != i):
                return [i, my_dict[diff]]
