class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return n
        
        i_len = [1]*n
        d_len = [1]*n
        
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                i_len[i] = i_len[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                d_len[i] = d_len[i+1]+1
                
        return max(max(i_len),max(d_len))
        
        # n = len(nums)
        # i,d = 1,1
        # for j in range(1,n):
        #     if nums[j]>nums[j-1]:
        #         i = i+1
        #         d = 1
        #     elif nums[j]<nums[j-1]:
        #         d = d+1
        #         i = 1
        #     else:
        #         i,d = 1,1
        # return max(i,d)
        