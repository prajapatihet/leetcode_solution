class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        i=0
        j=i+1
        while i<n:
            if i==n-1:
                return nums[i]
            if nums[i]==nums[j]:
                i+=2
                j+=2
            else:
                return nums[i]
                
            