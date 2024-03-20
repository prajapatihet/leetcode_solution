class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        m=len(matrix[0])

        mat=[]
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    mat.append((i,j))
        
        for r,c in mat:
            matrix[r]=[0]*m

            for i in range(n):
                matrix[i][c]=0
        