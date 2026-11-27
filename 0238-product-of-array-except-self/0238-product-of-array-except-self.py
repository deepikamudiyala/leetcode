class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pro=math.prod(nums)
        answer=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                answer[i]=pro//nums[i]
            else:
                pro1=math.prod(nums[0:i])*math.prod(nums[i+1:])
                answer[i]=pro1
        return answer