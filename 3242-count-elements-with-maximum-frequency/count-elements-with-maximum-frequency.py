class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m=0
        for k,v in d.items():
            if v>m:
                m=v
        c=0
        for k,v in d.items():
            if v==m:
                c+=m
        return c
