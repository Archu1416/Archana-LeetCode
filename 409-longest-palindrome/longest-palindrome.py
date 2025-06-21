class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for ch in s:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1
        l=0
        odd=False
        for k,v in d.items():
            if v%2==0:
                l+=v
            else:
                l+=v-1
                odd=True
        if odd:
            l+=1
        return l