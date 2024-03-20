class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        if(x<0):
            x=x*(-1)
            flag=1
        temp=x
        rev=0
        while temp:
            t=temp%10
            rev=rev*10+t
            temp=temp//10
        if flag:
            rev=rev*(-1)
        
        if rev > 2 ** 31 - 1 or rev < -(2 ** 31):
            return 0
        return rev