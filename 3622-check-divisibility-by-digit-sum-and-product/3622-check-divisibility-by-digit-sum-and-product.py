
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digisum=0
        digipro=1
        for i in str(n):
            digisum+=int(i)
            digipro*=int(i)
        return (n%(digisum+digipro)==0)