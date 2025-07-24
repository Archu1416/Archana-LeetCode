class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start=0
        i=0
        if not s:
            return True
        while start<len(t) and i<len(s):
            if t[start]==s[i]:
                i+=1
            start+=1
        if i==len(s):
            return True
        return False