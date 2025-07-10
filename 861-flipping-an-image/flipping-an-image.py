class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for row in image:
            r=[1-i for i in row[::-1]]
            res.append(r)
        return res