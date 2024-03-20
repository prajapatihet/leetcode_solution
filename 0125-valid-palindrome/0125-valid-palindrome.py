class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=list(s)
        n=len(lst)
        s=''
        for i in range(n):
            if lst[i].isalnum():
                s=s+lst[i].lower()  
        return s==s[::-1]
        