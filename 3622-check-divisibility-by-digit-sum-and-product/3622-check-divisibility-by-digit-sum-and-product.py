from math import prod
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits=[]
        for i in str(n):
            digits.append(int(i))

        digisum=sum(digits)
        digipro=prod(digits)
        return (n%(digisum+digipro)==0)