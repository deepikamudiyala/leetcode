class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res=1
        for l in range(len(nums)):
            pro=nums[l]
            gcd=nums[l]
            lcm=nums[l]
            for r in range(l+1,len(nums)):
                pro*=nums[r]
                gcd=math.gcd(gcd,nums[r])
                lcm=math.lcm(lcm,nums[r])
                if pro==(gcd*lcm):
                    res=max(res,r-l+1)
        return res