class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        #h=[x for x in nums]
        #heapq.heapify(h)
        #arr=[]
        #while h:
            #a=heapq.heappop(h)
            #b=heapq.heappop(h)
            #arr.append(b)
            #arr.append(a)
        #return arr
        nums.sort()
        for i in range(0,len(nums)-1,2):
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums