class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = nums.index(max(nums))
        min_num = nums.index(min(nums))
        if min_num>max_num:
            min_num,max_num=max_num,min_num
        res = min(max_num+1,n-min_num,min_num+1+n-max_num)
        return res