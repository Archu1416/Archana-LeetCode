class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for row in image:
            row.reverse()
            r=[]
            for i in row:
                r.append(1-i)
            res.append(r)
        return res