class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k=k1+k2
        d=[0]*len(nums1)
        for i in range (len(nums1)):
            d[i]=abs(nums1[i]-nums2[i])
        if sum(d)<=k:
            return 0
        d.sort(reverse=True)
        d.append(0)
        for i in range(1,len(nums1)+1):
            val=(d[i-1]-d[i])*i
            if val>k:
                q,r=divmod(k,i)
                h=d[i-1]-q 
                return (h*h*(i-r)+(h-1)*(h-1)*r+sum(x*x for x in d[i:len(nums1)]))
            k-=val
        return 0