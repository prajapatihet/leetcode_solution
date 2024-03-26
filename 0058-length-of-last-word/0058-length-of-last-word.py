class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        s = s.rstrip()
        n=len(s)
        for i in range(n-1,-1,-1):
            if s[i]==' ':
                break
            count+=1
        return count
                
        