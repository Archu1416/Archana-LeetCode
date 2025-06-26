class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val=0
        c=0
        p=1
        for i in range(len(s)-1,-1,-1):
            if s[i]=='0':
                c+=1
            else:
                if p+val<=k:
                    val+=p
                    c+=1
            p*=2
        return c