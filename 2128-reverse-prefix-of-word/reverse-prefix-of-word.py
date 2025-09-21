class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        res=""
        st=[]
        ind=word.index(ch)
        for i in range(ind+1):
            st.append(word[i])
        while st:
            res+=st.pop()
        for i in range(ind+1,len(word)):
            res+=word[i]
        return res
