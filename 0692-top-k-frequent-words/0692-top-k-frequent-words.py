class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count=Counter(words)
        h=[]
        ans=[]
        for s,freq in count.items():
            heapq.heappush(h,(-freq,s))
        for _ in range(k):
            freq,s=heapq.heappop(h)
            ans.append(s)
        return ans