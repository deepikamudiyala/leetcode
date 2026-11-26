class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums=set(nums)
        seq=0
        for x in nums:
            if x-1 not in nums:
                y=x+1
                while y in nums:
                    y+=1
                seq=max(seq,y-x)
        return seq

