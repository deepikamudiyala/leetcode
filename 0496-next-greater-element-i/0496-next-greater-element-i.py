class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        for i in range(len(nums1)):
            idx=nums2.index(nums1[i])
            j=idx+1
            temp=-1
            while(j<len(nums2)):
                if nums2[j]>nums1[i]:
                    temp=nums2[j]
                    break
                else:
                    j+=1
            nums1[i]=temp
        return nums1