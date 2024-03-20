class Solution:
    def isHappy(self, n: int) -> bool:
        sum=0
        while sum!=1 and sum!=4:
            sum =0
            while n!=0:
                rem = n%10
                n = n//10
                sum = sum+rem*rem
            n=sum
        
        if sum==1:
            return True
        else:
            return False