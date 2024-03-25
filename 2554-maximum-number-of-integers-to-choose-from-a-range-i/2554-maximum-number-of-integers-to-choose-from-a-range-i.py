class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        ans = 0
        total = 0
        ban = set(banned)
        
        for i in range(1,n+1):
            
            if i not in ban and maxSum>=total+i:
                ans+=1
                total+=i
        return ans
        