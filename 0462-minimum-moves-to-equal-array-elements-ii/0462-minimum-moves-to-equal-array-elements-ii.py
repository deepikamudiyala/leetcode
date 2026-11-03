class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=nums[len(nums)//2]
        ans=0
        for num in nums:
            ans+=abs(num-mid)
        return ans
