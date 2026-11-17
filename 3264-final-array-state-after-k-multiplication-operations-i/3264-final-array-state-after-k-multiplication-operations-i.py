class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k>0:
           a= nums.index(min(nums))
           nums[a]*=multiplier
           k-=1
        return nums
        #h=[(x,i) for i,x in enumerate(nums)]
        #heapq.heapify(h)
        #while k>0:
            ###val,i=h[0]
            #heapq.heapreplace(h,(val*multiplier,i))
            #k-=1
        #for val,i in h:
            #nums[i]=val
        #return nums