class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        x=""
        for i in str(n):
            if i!='0':
                x+=str(i)
                sum=sum+int(i)
        if n==0:
            return 0
        return  int(x)*int(sum)
       