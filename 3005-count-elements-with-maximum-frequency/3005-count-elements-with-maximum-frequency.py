class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency=[0]*101
        maxf=0
        for x in nums:
            frequency[x]+=1
            maxf=max(maxf, frequency[x])
        ans=0
        for f in frequency:
            if f==maxf:
                ans+=f
        return ans