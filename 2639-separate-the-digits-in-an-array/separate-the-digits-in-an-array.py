class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for n in nums:
            for ch in str(n):
                res.append(int(ch))
        return res