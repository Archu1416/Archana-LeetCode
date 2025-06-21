class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=n
        c=0
        if n==1:
            return 1
        for i in range(1,n+1):
            res-=i
            if res>=0:
                c+=1
            else:
                return c 