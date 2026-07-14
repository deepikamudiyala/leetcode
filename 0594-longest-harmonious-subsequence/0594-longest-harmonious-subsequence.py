class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        length=0
        for j in range(len(nums)):
            while nums[j]-nums[i]>1:
                i+=1
            if nums[j]-nums[i]==1:
                length=max(length,j-i+1)
        return length
            
