class Solution:
     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        n=len(nums1)
        nums1.sort()
        if n%2!=0:
            return nums1[n//2]
        else:
            return (nums1[(n-1)//2]+nums1[n//2])/2