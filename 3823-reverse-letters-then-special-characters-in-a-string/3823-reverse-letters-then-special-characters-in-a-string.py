class Solution:
    def reverseByType(self, s: str) -> str:
        n=len(s)
        res=list(s)
        i=0
        j=n-1
        while i<=j:
            if res[i].isalpha():
                if res[j].isalpha():
                    res[i],res[j]=res[j],res[i] 
                    i+=1
                    j-=1
                else:
                    j-=1
            else:
                i+=1
        a=0
        b=n-1
        while a<=b:
            if not res[a].isalpha():
                if not res[b].isalpha():
                    res[a],res[b]=res[b],res[a]
                    a+=1
                    b-=1
                else:
                    b-=1
            else:
                a+=1
        return ''.join(res)
        