class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for n in nums:
            re=[]
            while n!=0:
                r=n%10
                n=n//10
                re.append(r)
            for i in range(len(re)-1,-1,-1):
                res.append(re[i])
        return res