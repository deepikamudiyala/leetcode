class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        l=list(s)
        vowel=set('aeiouAEIOU')
        while i<=j:
            if l[i] in vowel:
                    if l[j] in vowel:
                        l[i],l[j]=l[j],l[i]
                        i+=1
                        j-=1
                    else:
                        j-=1
            else:
                i+=1
        return "".join(l)