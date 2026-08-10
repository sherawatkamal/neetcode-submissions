class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP, l, r = 0, 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                continue
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
            r += 1
        return maxP
            
            