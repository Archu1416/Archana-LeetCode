class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res=[]
        s1=s1.split()
        s2=s2.split()
        d1={}
        d2={}
        for i in s1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in s2:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for k,v in d1.items():
            if v==1 and k not in s2:
                res.append(k)
        for k,v in d2.items():
            if v==1 and k not in s1:
                res.append(k)
        return res
        