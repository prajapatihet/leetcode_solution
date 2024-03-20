class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1=list(s)
        s2=list(t)
        n=len(s2)
        m=len(s1)
        ans=''
        if not m:
            return t
        while n:
            rem=s2.pop()
            if rem not in s1:
                ans+=rem
                break    
            else:
                s1.remove(rem)
                 
        return ans

        