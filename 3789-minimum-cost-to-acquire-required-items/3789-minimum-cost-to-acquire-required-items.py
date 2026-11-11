class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        cost=0
        if cost1+cost2<=costBoth:
            cost=need1*cost1+need2*cost2
        else:
            cost3=min(need1,need2)
            cost=costBoth*cost3
            need1-=cost3
            need2-=cost3
            if need1>0:
                cost+=need1*min(cost1,costBoth)
            elif need2>0:
                cost+=need2*min(cost2,costBoth)
        return cost
