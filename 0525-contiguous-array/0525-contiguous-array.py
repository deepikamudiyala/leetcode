class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={0:-1}
        sum=0
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                sum-=1
            else:
                sum+=1
            if sum in d:
                res=max(res,i-d[sum])
            else:
                d[sum]=i
        return res
                