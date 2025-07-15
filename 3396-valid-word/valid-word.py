class Solution:
    def isValid(self, word: str) -> bool:
        word=word.lower()
        v=c=d=0
        if  len(word)>=3:
            for i in word:
                if i>='a' and i<='z':
                    if i in ['a','e','i','o','u']:
                       v+=1
                    else:
                        c+=1
                elif i.isdigit():
                    d+=1
                else:
                    return False
        if v and c:
            return True
        return False