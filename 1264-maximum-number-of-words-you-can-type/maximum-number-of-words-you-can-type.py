class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text=text.split()
        c=0
        for word in text:
            for i in brokenLetters:
                if i in word:
                    c+=1
                    break
        return len(text)-c