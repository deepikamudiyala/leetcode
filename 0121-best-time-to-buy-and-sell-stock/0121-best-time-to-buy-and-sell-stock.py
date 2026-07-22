class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        j=prices[0]
        profit=0
        for i in range(len(prices)):
            pro=prices[i]-j
            profit=max(profit,pro)
            j=min(prices[i],j)
        return profit