class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        min_val = prices[0]

        for price in prices:
            maxP = max(maxP, price - min_val)
            min_val = min(min_val, price)
        
        return maxP