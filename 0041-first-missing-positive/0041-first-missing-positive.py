class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=set(nums)
        x=1
        while x in num:
            x+=1
        return x
        