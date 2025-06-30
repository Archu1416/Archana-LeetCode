from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max=0
        if not nums:
            return 0
        c=Counter(nums)
        for i in nums:
            if i+1 in nums:
                s=c[i]+c[i+1]
                if s>max:
                    max=s
        return max