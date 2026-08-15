import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r, res = 1, max(piles), 1

        while l <= r:
            m = l + ((r - l)//2)
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours > h:
                l = m + 1
            else:
                r = m - 1
                res = m
        return res
