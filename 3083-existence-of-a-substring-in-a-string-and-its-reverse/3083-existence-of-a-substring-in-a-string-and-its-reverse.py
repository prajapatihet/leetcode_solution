class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        if len(s)<2:
            return False
        n=len(s)
        for a in range(n-1):
            for b in range(a+1,n):
                sub = s[a:b+1]
                reverse = sub[::-1]
                if reverse in s:
                    return True
        return False
        
        