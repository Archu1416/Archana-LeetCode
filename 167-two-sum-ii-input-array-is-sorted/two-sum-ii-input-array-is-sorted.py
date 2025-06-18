class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            t=nums[l]+nums[r]
            if t==target:
                return [l+1,r+1]
            elif t>target:
                r-=1
            else:
                l+=1
                