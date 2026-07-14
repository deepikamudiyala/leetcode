class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c=0
        for i in range(k):
            if blocks[i]=='W':
                c+=1
        res=c
        for i in range(k,len(blocks)):
            if blocks[i-k]=='W':
                c-=1
            if blocks[i]=='W':
                c+=1
            res=min(res,c)
        return res

