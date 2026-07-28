class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        left=0
        right=sum(nums)
        count=0
        for i in range(len(nums)):
            left+=nums[i]
            right-=nums[i]
            if nums[i]!=0:
                continue
            if left==right:
                count+=2
            if abs(left-right)==1:
                count+=1
        return count