class Solution:
    def reverseVowels(self, s: str) -> str:
        v="aeiouAEIOU"
        lst=list(s)
        l,r=0,len(s)-1
        while l<r:
            while l<r and lst[l] not in v:
                l+=1
            while l<r and lst[r] not in v:
                r-=1
            lst[l],lst[r]=lst[r],lst[l]
            l+=1
            r-=1
        return ''.join(lst)