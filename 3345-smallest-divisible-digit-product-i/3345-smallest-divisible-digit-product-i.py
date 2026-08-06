class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        while(n):
            temp=n
            prod=1
            while(temp>0):
                prod=prod*(temp%10)
                temp=temp//10
            if(prod%t==0):
                return n
            n+=1
