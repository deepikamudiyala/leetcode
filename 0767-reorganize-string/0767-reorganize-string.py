class Solution:
    def reorganizeString(self, s: str) -> str:
        h=[]
        count=Counter(s)
        for s,f in count.items():
            heapq.heappush(h,(-f,s))
        res=""
        while len(h)>1:
            f1,ch1=heapq.heappop(h)
            f2,ch2=heapq.heappop(h)
            res+=ch1
            res+=ch2
            if f1+1<0:heapq.heappush(h,(f1+1,ch1))
            if f2+1<0:heapq.heappush(h,(f2+1,ch2))
        if h:
            f,ch=heapq.heappop(h)
            if -f>1:
                return ""
            res+=ch
        return res
