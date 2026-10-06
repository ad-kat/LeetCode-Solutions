class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS=len(matrix), len(matrix[0])
        rows, cols= [False]*ROWS, [False]*COLS
        for i in range(0,ROWS):
            for j in range(0, COLS):
                if matrix[i][j]==0:
                    rows[i]=True
                    cols[j]= True
        for i in range(ROWS):
            for j in range(COLS):
                if rows[i] or cols[j]:
                    matrix[i][j]=0

        