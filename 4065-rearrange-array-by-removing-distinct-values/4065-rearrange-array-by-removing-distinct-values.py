class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        count=Counter(nums)
        while count:
            ans+=sorted(count)
            count-=Counter(count.keys())
        return ans
