
class Solution:
    def isUgly(self, n: int) -> bool:
        # while n >= 1:
        #     if n%2 == 0:
        #          n=n//2
        #     elif n%3 == 0:
        #         n=n//3
        #     elif n%5 == 0:
        #         n=n//5
        #     elif n == 1:
        #         return True
        #     else:
        #         return False
        # return False
        if n == 0: 
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n //= i

        return n == 1     
        