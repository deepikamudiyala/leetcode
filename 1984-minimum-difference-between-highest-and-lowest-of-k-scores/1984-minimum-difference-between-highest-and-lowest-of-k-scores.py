class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        mini=nums[k-1]-nums[0]
        for r in range(len(nums)-k+1):
            mini=min(mini,nums[r+k-1]-nums[r])
        return mini