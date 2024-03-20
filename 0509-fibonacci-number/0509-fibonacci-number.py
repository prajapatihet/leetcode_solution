class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        n0=0
        n1=1
        c=1
        while c<n:
            n2=n0+n1
            n0=n1
            n1=n2
            c+=1
        return n2

        