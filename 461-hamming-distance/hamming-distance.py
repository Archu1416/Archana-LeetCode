class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        b1=bin(x)[2:]
        b2=bin(y)[2:]
        c=0
        n=max(len(b1),len(b2))
        b1=b1.zfill(n)
        b2=b2.zfill(n)
        for i in range(n):
            if b1[i]!=b2[i]:
                c+=1
        return c