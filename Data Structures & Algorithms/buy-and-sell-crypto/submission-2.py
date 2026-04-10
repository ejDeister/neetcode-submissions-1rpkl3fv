class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        maxp = 0
        for p in prices:
            maxp = max(maxp,p-buy)
            buy = min(buy,p)
        return maxp
