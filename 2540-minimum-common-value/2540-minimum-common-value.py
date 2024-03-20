class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)<1 or len(nums2)<1:
            return -1
        a=set(nums1)
        b=set(nums2)
        c=a.intersection(b)

        if len(c)<1:
            return -1
        return min(c)