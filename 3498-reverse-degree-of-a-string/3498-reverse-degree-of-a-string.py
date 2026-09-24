class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i,n in enumerate(s):
            rev=26-(ord(n)-ord('a'))
            pos=i+1
            res+=rev*pos
        return res