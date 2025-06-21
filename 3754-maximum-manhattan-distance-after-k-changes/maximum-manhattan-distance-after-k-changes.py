class Solution:
    def maxDistance(self, st: str, k: int) -> int:
        e=w=s=n=0
        res=0
        for i in range(len(st)):
            if st[i]=='E':
                e+=1
            elif st[i]=='W':
                w+=1
            elif st[i]=='S':
                s+=1
            else:
                n+=1
            res=max(res,min(abs(s-n)+abs(e-w)+2*k,i+1))
        return res