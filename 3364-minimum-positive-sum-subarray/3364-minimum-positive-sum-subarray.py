class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res=float('inf')
        for i in range(l,r+1):
            summ=sum(nums[:i])
            if summ>0:
                res=min(res,summ)
            for j in range(i,len(nums)):
                summ=summ+nums[j]-nums[j-i]
                if summ>0:
                    res=min(res,summ)
        if res==float('inf'):
            return -1
        return res
            