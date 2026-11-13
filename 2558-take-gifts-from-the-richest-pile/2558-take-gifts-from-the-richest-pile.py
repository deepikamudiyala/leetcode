class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h=[-x for x in gifts]
        heapq.heapify(h)
        i=1
        while i<=k:
            a=-heapq.heappop(h)
            heapq.heappush(h,-floor(sqrt(a)))
            i+=1
        return -sum(h)