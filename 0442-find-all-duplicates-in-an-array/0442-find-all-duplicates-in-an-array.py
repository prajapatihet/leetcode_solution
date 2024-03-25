class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<2:
            return []
        s=set()
        ans=[]
        for i in range(n):
            if nums[i] in s:
                ans.append(nums[i])
            else:
                s.add(nums[i])
        return ans