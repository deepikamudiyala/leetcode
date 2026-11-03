class Solution:
    def minMoves(self, nums: List[int]) -> int:
        ans=0
        maxx=max(nums)
        for i in nums:
            ans+=maxx-i
        return ans