class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        h=[x for x in nums]
        heapq.heapify(h)
        arr=[]
        while h:
            a=heapq.heappop(h)
            b=heapq.heappop(h)
            arr.append(b)
            arr.append(a)
        return arr