class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0])!=r*c:
            return mat
        t=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                t.append(mat[i][j])
        x=0
        ans=[]
        for i in range(r):
            q=[]
            for j in range(c):
                q.append(t[x])
                x+=1
            ans.append(q)
        return ans
