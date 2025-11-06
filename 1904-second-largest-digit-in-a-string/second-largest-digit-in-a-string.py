class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=[]
        for ch in s:
            if ch=='1' or ch=='2' or ch=='0' or ch=='3' or ch=='4' or ch=='5' or ch=='6' or ch=='7' or ch=='8' or ch=='9':
                lst.append(int(ch))
        l=s=float('-inf')
        for i in lst:
            if i>l:
                s=l
                l=i
            elif i>s and i!=l:
                s=i
        return s if s!=float('-inf') else -1