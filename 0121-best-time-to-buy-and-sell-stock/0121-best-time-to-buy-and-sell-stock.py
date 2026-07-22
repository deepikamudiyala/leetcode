class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<j:
                j=prices[i]
            profit=max(profit,prices[i]-j)
            
        return profit