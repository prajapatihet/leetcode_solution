class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n>0:
            temp=n
            if n==1:
                return True
            if n==2  or n==3:
                return False
            count=0
            while n:
                n//=4
                count+=1
                if n==1 or n==2 or n==3:
                    if temp==4**count:
                        return True
                    return False
            return True
        return False
        