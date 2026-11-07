class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        d=set()
        k=0
        for x in nums:
            if x in d:
                k^=x
            d.add(x)
        return k