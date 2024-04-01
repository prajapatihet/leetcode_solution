class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        sums=0
        while temp:
            tmp = temp%10
            sums+=tmp
            temp//=10
        if x%sums==0:
            return sums
        else:
            return -1
            
        