class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        heap=[]
        for i in range(len(score)):
            heapq.heappush(heap,(-score[i],i))
        res=[""]*len(score)
        rank=0
        while heap:
            val,idx=heapq.heappop(heap)
            rank+=1
            if rank==1:
                res[idx]="Gold Medal"
            elif rank==2:
                res[idx]="Silver Medal"
            elif rank==3:
                res[idx]="Bronze Medal"
            else:
                res[idx]=str(rank)
        return res