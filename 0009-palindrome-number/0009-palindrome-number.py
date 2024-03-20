class Solution:
    def isPalindrome(self, x: int) -> bool:
        num2=x
        num=0
        s=str(x)
        if not s.isdigit():
            return False
        while x:
            temp=x%10
            num=num*10+temp
            x=x//10

        if num==num2:
            return True
        else:
            return False