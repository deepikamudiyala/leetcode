class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        a=nums[::-1]
        res=nums
        for i in range(len(nums)):
            res.append(a[i])
        return res