class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        index = n//2
        
        ops = 0
        
        for i in range(n):
            if nums[i]<k and index<=i:
                ops+=k-nums[i]
            elif nums[i]>k and index>=i:
                ops+=nums[i]-k
        return ops