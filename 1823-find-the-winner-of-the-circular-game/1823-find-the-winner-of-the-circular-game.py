class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def reccursion(n,k):
            if n==1:
                return 0
            return (reccursion(n-1,k)+k)%n
        return reccursion(n,k)+1