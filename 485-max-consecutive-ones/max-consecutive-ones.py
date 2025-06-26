class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        r=[]
        for i in nums:
            if i==1:
                c+=1
            else:
                r.append(c)
                c=0
        r.append(c)
        return max(r)