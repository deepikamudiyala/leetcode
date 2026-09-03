class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=0
        odd=0
        modd=float('inf')
        meven=float('inf')
        for i in nums1:
            if i%2==0:
                even+=1
                meven=min(meven,i)
            else:
                odd+=1
                modd=min(modd,i)
        return even==len(nums1) or odd==len(nums1) or meven>modd
            
            