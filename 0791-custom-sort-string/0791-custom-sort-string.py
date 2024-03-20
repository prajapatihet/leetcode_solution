class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans=''
        l1=list(order)
        l2=list(s)
        p=len(s)
        n=len(l1)
        for i in range(n):
            j=0
            while j<p:
                if l1[i] in l2:
                    ans+=l1[i]
                    l2.remove(l1[i])
                j+=1
        m=len(l2)
        for i in range(m):
            ans+=l2[i]
        
        return ans