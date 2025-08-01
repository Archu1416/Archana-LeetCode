class Solution:
    def generate(self, n: int) -> List[List[int]]:
        lst=[[1]*(i+1) for i in range(n) ]
        for i in range(2,n):
            for j in range(1,i):
                lst[i][j]=lst[i-1][j-1]+lst[i-1][j]
        return lst