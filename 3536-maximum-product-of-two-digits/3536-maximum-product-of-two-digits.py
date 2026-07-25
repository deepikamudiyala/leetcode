class Solution:
    def maxProduct(self, n: int) -> int:
        a=[int(i) for i in str(n)]
        a.sort()
        return a[-1]*a[-2]