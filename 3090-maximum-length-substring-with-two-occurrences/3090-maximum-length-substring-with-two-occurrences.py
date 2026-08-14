class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            a={}
            for j in range(i,len(s)):
                if s[j] not in a:
                    a[s[j]]=0
                a[s[j]]+=1
                if a[s[j]]>2:
                    break
                res=max(res,j-i+1)
        return res