class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            nums[i]*=nums[i]
        
        nums.sort()
        ans+=sum(nums[n//2:])
        ans-=sum(nums[:n//2])
        return ans