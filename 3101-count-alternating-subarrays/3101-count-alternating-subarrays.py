class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        c=0
        l=0
        
        for r in range(len(nums)):
            if r>0 and nums[r] == nums[r-1]:
                l=r
            c+=r-l+1
        return c