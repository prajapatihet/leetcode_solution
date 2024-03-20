class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[-1]*n
        stack=[]
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
        return ans
        