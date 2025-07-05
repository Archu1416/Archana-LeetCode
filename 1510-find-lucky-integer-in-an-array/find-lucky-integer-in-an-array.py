class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        r=0
        for k,v in d.items():
            if k==v:
                if r<v:
                    r=v
        if r:
            return r
        return -1