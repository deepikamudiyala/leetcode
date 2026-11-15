class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9+7
        count=presum=0
        odd=0
        even=1
        for num in arr:
            presum+=num
            if presum%2==0:
                count+=odd
                even+=1
            else:
                count+=even
                odd+=1
            count%=mod
        return count