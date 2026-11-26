class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d={0:1}
        pre=0
        count=0
        for num in nums:
            pre+=num
            if pre-k in d:
                count+=d[pre-k]
            d[pre]=d.get(pre,0)+1
        return count