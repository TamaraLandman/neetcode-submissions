class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_marks = [False] * rows
        col_marks = [False] * cols

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    row_marks[row] = True
                    col_marks[col] = True
        
        for row in range(rows):
            for col in range(cols):
                if row_marks[row] == True or col_marks[col] == True:
                    matrix[row][col] = 0

        #return matrix

        
        