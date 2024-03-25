class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        i=0
        j=i+1
        m=0
        while i<n:
            if i==n-1:
                m=nums[i]
                break
            elif nums[i]==nums[j]:
                i+=2
                j+=2
            else:
                m=nums[i]
                break
        return m
        