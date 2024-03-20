import math
class Solution:
    def divide(self, a: int, b: int) -> int:
        temp=a/b
        if temp>=0:
            if (a==(-2147483648) and b==(-1)):
                return math.floor(temp)-1
            return math.floor(temp)
        else:
            return math.ceil(temp)
            