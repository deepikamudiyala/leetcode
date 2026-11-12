class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxx=0
        increase=1
        decrease=1
        if len(nums)==1:return 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                increase+=1
                decrease=1
            elif nums[i]<nums[i-1]:
                increase=1
                decrease+=1
            else:
                increase=decrease=1
            maxx=max(maxx,increase,decrease)
        return maxx