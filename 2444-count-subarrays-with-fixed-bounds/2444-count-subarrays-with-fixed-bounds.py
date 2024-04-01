class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # if nums[0]>maxK:
        #     return 0
        # for i in range(len(nums)):
        #     if nums[i]>maxK:
        #         break
        n = len(nums)
        ans = 0
        minindex = -1
        maxindex = -1
        index = -1

        for i in range(n):
            if nums[i] < minK or nums[i] > maxK:
                index = i

            if nums[i] == minK:
                minindex = i

            if nums[i] == maxK:
                maxindex = i

            smaller = min(minindex, maxindex)
            temp = smaller - index

            ans += temp if temp > 0 else 0

        return ans
        