class Solution:
    def countCommas(self, n: int) -> int:
        return max(n-999,0)+max(0,n-999999)+max(0,n-999999999)+max(0,n-999999999999)+max(0,n-999999999999999)
       