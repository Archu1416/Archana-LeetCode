class Solution:
    def kthCharacter(self, k: int) -> str:
        s="a"
        while len(s)<k:
            t=""
            for i in range(len(s)):
                t+=chr(ord(s[i])+1)
            s+=t
        return s[k-1]