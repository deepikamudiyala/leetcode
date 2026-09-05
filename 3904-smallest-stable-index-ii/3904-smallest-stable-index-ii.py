class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        premax=[0]*len(nums)
        premin=[0]*len(nums)
        maxi=float('-inf')
        for i in range(len(nums)):
            if nums[i]>maxi:
                maxi=nums[i]
            premax[i]=maxi
        mini=float('inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<mini:
                mini=nums[i]
            premin[i]=mini
        for i in range(len(nums)):
            if premax[i]-premin[i]<=k:
                return i
        return -1