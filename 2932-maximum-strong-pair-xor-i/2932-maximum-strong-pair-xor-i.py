class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        xor=0
        j=0
        nums.sort()
        for i in range(len(nums)):
            while nums[i]>2*nums[j]:
                j+=1
            for k in range(j,i):
                xor=max(xor,nums[i]^nums[k])
        return xor
        