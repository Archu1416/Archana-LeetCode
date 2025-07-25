class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res=[]
        for i in nums:
            if i not in res and i>0:
                res.append(i)
        if len(res)==0:
            return max(nums)
        return sum(res)