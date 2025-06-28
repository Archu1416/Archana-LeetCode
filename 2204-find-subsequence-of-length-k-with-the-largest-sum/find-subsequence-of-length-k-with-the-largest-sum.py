class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        r=[]
        for i in range(len(nums)):
            r.append([nums[i],i])
        r.sort(reverse=True,key=lambda x: x[0])
        vals=r[:k]
        vals.sort(key=lambda x: x[1])
        res=[]
        for i in vals:
            res.append(i[0])
        return res