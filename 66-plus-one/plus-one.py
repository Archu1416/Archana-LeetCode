class Solution:
    def plusOne(self, digits: List[int]):
        s=""
        for i in digits:
            s+=str(i)
        n=int(s)+1
        r=[]
        while n!=0:
            rem=n%10
            r.append(rem)
            n=n//10
        r.reverse()
        return r