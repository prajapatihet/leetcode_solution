class Solution:
    def helper(self,n,dp):
        if n<=1:
            return 1
        # Otimized the code using dp
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.helper(n-1,dp)+self.helper(n-2,dp)
        return dp[n]
    def climbStairs(self, n: int) -> int:
        # initinized dp array
        dp=[-1 for i in range(n+1)]
        return self.helper(n,dp)
        