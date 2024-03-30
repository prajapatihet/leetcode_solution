class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        c={}
        for num in nums:
            c[num] = c.get(num,0)+1

        res=[]

        for num,count in c.items():
            if count > n//3:
                res.append(num)

        return res
        