class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        minimum = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(minimum, nums[l])
                break
            m = l + ((r - l)//2)
            minimum = min(minimum, nums[m])
            if nums[m] < nums[l]:
                r = m - 1
            else:
                l = m + 1
        return minimum
