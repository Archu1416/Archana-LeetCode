class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        r=0
        for i in range(k.bit_length()-1,-1,-1):
            if (k-1) & (1<<i):
                r+=operations[i]
        return chr(ord("a")+(r%26))