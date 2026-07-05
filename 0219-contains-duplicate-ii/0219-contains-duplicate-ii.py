class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ans={}
        for i,n in enumerate(nums):
            if n in ans and i-ans[n]<=k:
                return True
            ans[n]=i
        return False
        
        