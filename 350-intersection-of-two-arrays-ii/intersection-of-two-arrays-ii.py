from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1=Counter(nums1)
        r=[]
        for i in nums2:
            if c1[i]>0:
                r.append(i)
                c1[i]-=1
        return r