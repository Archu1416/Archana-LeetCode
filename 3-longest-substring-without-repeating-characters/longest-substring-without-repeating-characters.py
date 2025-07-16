class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=[]
        l=0
        for i in range(len(s)):
            if s[i] not in r:
                r.append(s[i])
            else:
                l=max(len(r),l)
                while s[i] in r:
                    r.pop(0)
                r.append(s[i])
        return max(len(r),l)