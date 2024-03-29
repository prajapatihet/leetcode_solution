class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f = {}
        n = len(nums)
        final = 0
        i = 0
        j = 0
        while j < n:
            f[nums[j]] = f.get(nums[j], 0) + 1
            while f[nums[j]] > k:
                f[nums[i]] -= 1
                i += 1
            final = max(final, j - i + 1)
            j += 1
        return final