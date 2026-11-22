class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count=Counter(tasks)
        heap=[(-freq) for val,freq in count.items()]
        heapq.heapify(heap)
        time=0
        q=deque()
        while heap or q:
            time+=1
            if heap:
                cnt=heapq.heappop(heap)+1
                if cnt:
                    q.append((cnt,time+n))
            if q and q[0][1]==time:
                heapq.heappush(heap,q.popleft()[0])
        return time
        
           