class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        m=10**9+7
        n=len(nums)
        nums.sort()
        p=[1]*n
        for i in range(1,n):
            p[i]=(p[i-1]*2)%m
        res=0
        l,r=0,n-1
        while l<=r:
            if nums[l]+nums[r]<=target:
                c=p[r-l]
                res=(res+c)%m
                l+=1
            else:
                r-=1
        return res