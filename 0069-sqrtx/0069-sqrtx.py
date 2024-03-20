class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x-1
        mid=0
        if x==1 or x==0:
            return x
        while l<=r:
            mid=r-(r-l)//2
            q=mid*mid  
            if q==x:
                return mid
            elif q>x:
                r=mid-1
            else:
                l=mid+1
        return r
        
        