class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a={}
        for i in magazine:
                a[i]=a.get(i,0)+1
        for i in ransomNote:
            if a.get(i,0)==0:
                return False
            a[i]-=1
        return True