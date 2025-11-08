class Solution:
    def reverseWords(self, s: str) -> str:
        a=s.split()
        res=""
        res=' '.join(a[::-1])
        return res