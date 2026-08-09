class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = 0

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                return abs(nums[i])
            else:
                nums[index] = - nums[index]