from collections import defaultdict
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d=defaultdict(int)
        for i in word:
            d[i]+=1
        cnt=list(d.values())
        res=len(word)
        for i in cnt:
            dlt=0
            for j in cnt:
                if j<i:
                    dlt+=j
                elif j>i+k:
                    dlt+=j-(i+k)
            res=min(res,dlt)
        return res