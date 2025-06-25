class Solution:
    def findComplement(self, num: int) -> int:
        b=bin(num)[2:]
        r=""
        for i in b:
            if i=='0':
                r+='1'
            else:
                r+='0'
        return int(r,2)