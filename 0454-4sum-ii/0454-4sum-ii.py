class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        res=0
        d=defaultdict(int)
        n=len(nums1)
        for i in range(n):
            for j in range(n):
                d[nums1[i]+nums2[j]]+=1
        for k in range(n):
            for l in range(n):
                res+=d[0-(nums3[k]+nums4[l])]
        return res