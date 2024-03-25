class Solution:
    def arraySign(self, nums: List[int]) -> int:
        n=len(nums)
        if 0 in nums:
            return 0
        ans=1
        for i in range(n):
            if nums[i]<0:
                nums[i]=-1
                ans=ans*nums[i]
            else:
                nums[i]=1
        return ans