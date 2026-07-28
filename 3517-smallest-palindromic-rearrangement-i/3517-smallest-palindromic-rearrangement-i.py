class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)//2
        res=sorted(s[:n])
        mid=[s[n]] if len(s)%2==1 else []
        rev=res[::-1]
        return "".join(res+mid+rev)