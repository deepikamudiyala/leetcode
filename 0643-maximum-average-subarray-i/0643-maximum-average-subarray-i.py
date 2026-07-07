class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=sum(nums[:k])
        maxsum=summ
        for i in range(k,len(nums)):
            summ=summ+nums[i]-nums[i-k]
            maxsum=max(summ,maxsum)
        return maxsum/k
