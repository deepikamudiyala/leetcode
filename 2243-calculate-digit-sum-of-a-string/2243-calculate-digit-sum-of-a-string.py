class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            a=[]
            n=len(s)
            for i in range(0,n,k):
                sum=0
                for j in range(i,min(i+k,n)):
                    sum+=int(s[j])
                a.append(str(sum))
            s="".join(a)
        return s
