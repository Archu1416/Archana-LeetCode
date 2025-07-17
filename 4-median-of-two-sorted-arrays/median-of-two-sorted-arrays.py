class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=sorted(nums1+nums2)
        sum=0
        lst.sort()
        mid=len(lst)//2
        if len(lst)%2==0:
            return (lst[mid-1]+lst[mid])/2
        else:
            return lst[mid]