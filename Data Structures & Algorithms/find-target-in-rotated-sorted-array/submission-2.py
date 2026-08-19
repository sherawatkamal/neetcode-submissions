class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivot_index = l
        
        l, r = 0, len(nums) - 1

        if target == nums[pivot_index]:
            return  pivot_index
        elif target <= nums[r]:
            l = pivot_index + 1
        else:
            r = pivot_index - 1

        while l <= r:
            m = l + ((r - l)//2)
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return - 1
        
