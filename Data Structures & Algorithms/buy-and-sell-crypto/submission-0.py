class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minim = 0
        maxim = 1
        best = 0
        for i in range(1,len(prices)):
            print(i, prices[minim], prices[maxim], best)
            if prices[i] < prices[minim]:
                if i+1 < len(prices):
                    print(best)
                    minim = i
                    maxim = i+1
            elif prices[i] > prices[maxim]:
                maxim = i
            best = max(best, prices[maxim] - prices[minim]) 
        return best